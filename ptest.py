import sys
import subprocess
import re
import os
from collections import defaultdict
import json
import pathlib
import stat
import shutil
from glob import glob

import click
import pytest
from pytest_jsonreport.plugin import JSONReport


task_dirs = [
    "04_data_structures",
    "05_basic_scripts",
    "06_control_structures",
    "07_files",
    "09_functions",
    "11_modules",
    "12_useful_modules",
    "15_module_re",
    "17_serialization",
    "18_ssh_telnet",
    "19_concurrent_connections",
    "20_jinja2",
    "21_textfsm",
    "22_oop_basics",
    "23_oop_special_methods",
    "24_oop_inheritance",
]


class PtestError(Exception):
    """
    Ошибка в использовании/работе скрипта ptest
    """


def red(msg):
    return click.style(msg, fg="red")


def green(msg):
    return click.style(msg, fg="green")


def exception_handler(exception_type, exception, traceback):
    """
    sys.excepthook для отключения traceback по умолчанию
    """
    print(f"\n{exception_type.__name__}: {exception}\n")


class CustomTasksType(click.ParamType):
    """
    Класс создает новый тип для click и преобразует
    допустимые варианты строк заданий в отдельные файлы тестов.

    Кроме того проверяет есть ли такой файл в текущем каталоге
    и оставляет только те, что есть.
    """

    def convert(self, value, param, ctx):
        regex = (
            r"(?P<all>all)|"
            r"(?P<number_star>\d\*)|"
            r"(?P<letters_range>\d[a-i]-[a-i])|"
            r"(?P<numbers_range>\d-\d)|"
            r"(?P<single_task>\d[a-i]?)"
        )
        current_chapter = current_dir_name()
        if current_chapter not in task_dirs:
            task_dirs_line = "\n    ".join(task_dirs)
            self.fail(
                red(
                    f"\nСкрипт нужно вызывать из каталогов с заданиями:"
                    f"\n    {task_dirs_line}"
                )
            )

        current_chapter = current_chapter_id()
        tasks_list = re.split(r"[ ,]+", value)
        test_files = []
        for task in tasks_list:
            match = re.fullmatch(regex, task)
            if match:
                if task == "all":
                    return value
                else:
                    if match.group("letters_range"):
                        task = f"{task[0]}[{task[1:]}]"  # convert 1a-c to 1[a-c]
                    elif match.group("numbers_range"):
                        task = f"[{task}]"  # convert 1-3 to [1-3]

                    test_files += glob(f"test_task_{current_chapter}_{task}.py")
            else:
                self.fail(
                    red(
                        f"Данный формат не поддерживается {task}. "
                        "Допустимые форматы: 1, 1a, 1b-d, 1*, 1-3"
                    )
                )
        return test_files


def call_command(command, verbose=True, return_stdout=False):
    """
    Функция вызывает указанную command через subprocess
    и выводит stdout и stderr, если флан verbose=True.
    """
    result = subprocess.run(
        command,
        shell=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
    )
    std = result.stdout
    if return_stdout:
        return std
    if verbose:
        print("#" * 20, command)
        if std:
            print(std)
    return result.returncode


def current_chapter_id():
    """
    Функция возвращает номер текущего раздела, где вызывается ptest.
    """
    pth = str(pathlib.Path().absolute())
    last_dir = os.path.split(pth)[-1]
    current_chapter = int(last_dir.split("_")[0])
    return current_chapter


def current_dir_name():
    pth = str(pathlib.Path().absolute())
    current_chapter_name = os.path.split(pth)[-1]
    return current_chapter_name


def parse_json_report(report):
    """
    Отбирает нужные части из отчета запуска pytest в формате JSON.
    Возвращает список тестов, которые прошли.
    """
    if report and report["summary"]["total"] != 0:
        all_tests = defaultdict(list)
        summary = report["summary"]

        test_names = [test["nodeid"] for test in report["collectors"][0]["result"]]
        for test in report["tests"]:
            name = test["nodeid"].split("::")[0]
            all_tests[name].append(test["outcome"] == "passed")
        all_passed_tasks = [name for name, outcome in all_tests.items() if all(outcome)]
        return all_passed_tasks
    else:
        return []


def copy_answers(passed_tasks):
    """
    Функция клонирует репозиторий с ответами в домашний каталог пользователя
    копирует ответы для заданий, которые прошли тесты.
    После того как ответы скопированы, репозиторий с ответами удаляется.
    Все это выполняется вручную, а не через tempfile, из-за проблем
    с удалением на Windows.
    """
    pth = str(pathlib.Path().absolute())
    current_chapter_name = os.path.split(pth)[-1]
    current_chapter_number = int(current_chapter_name.split("_")[0])

    homedir = pathlib.Path.home()
    os.chdir(homedir)
    returncode = call_command(
        "git clone --depth=1 https://github.com/natenka/pyneng-answers",
        verbose=False,
    )
    if returncode == 0:
        os.chdir(f"pyneng-answers/answers/{current_chapter_name}")
        copy_answer_files(passed_tasks, pth)
        print(
            green(
                "\nОтветы на задания, которые прошли тесты "
                "скопированы в файлы answer_task_x.py\n"
            )
        )
        os.chdir(homedir)
        shutil.rmtree("pyneng-answers", onerror=remove_readonly)
    else:
        raise PtestError(red("Не получилось скопировать ответы."))
    os.chdir(pth)


def remove_readonly(func, path, _):
    """
    Вспомогательная функция для Windows, которая позволяет удалять
    read only файлы из каталога .git
    """
    os.chmod(path, stat.S_IWRITE)
    func(path)


def copy_answer_files(passed_tasks, pth):
    """
    Функция копирует ответы для указанных заданий.
    """
    for test_file in passed_tasks:
        task_name = test_file.replace("test_", "")
        answer_name = test_file.replace("test_", "answer_")
        if not os.path.exists(f"{pth}/{answer_name}"):
            call_command(
                f"cp {task_name} {pth}/{answer_name}",
                verbose=False,
            )


@click.command(
    context_settings=dict(
        ignore_unknown_options=True, help_option_names=["-h", "--help"]
    )
)
@click.argument("tasks", default="all", type=CustomTasksType())
@click.option(
    "--disable-verbose", "-d", is_flag=True, help="Отключить подробный вывод pytest"
)
@click.option(
    "--answer",
    "-a",
    is_flag=True,
    help=(
        "Скопировать ответы для заданий, которые "
        "прошли тесты. При добавлении этого флага, "
        "не выводится traceback для тестов."
    ),
)
@click.option("--debug", is_flag=True, help="Показывать traceback исключений")
def cli(tasks, disable_verbose, answer, debug):
    """
    Запустить тесты для заданий TASKS. По умолчанию запустятся все тесты.

    Примеры запуска:

    \b
        ptest            запустить все тесты для текущего раздела
        ptest 1,2a,5     запустить тесты для заданий 1, 2a и 5
        ptest 1,2a-c,5   запустить тесты для заданий 1, 2a, 2b, 2c и 5
        ptest 1,2*       запустить тесты для заданий 1, все задания 2 с буквами и без
        ptest 1,3-5      запустить тесты для заданий 1, 3, 4, 5
        ptest 1-5 -a     запустить тесты и записать ответы на задания,
                         которые прошли тесты, в файлы answer_task_x.py

    Флаг -d отключает подробный вывод pytest, который включен по умолчанию.
    Флаг -a записывает ответы в файлы answer_task_x.py, если тесты проходят.
    """
    if not debug:
        sys.excepthook = exception_handler

    json_plugin = JSONReport()
    pytest_args_common = ["--json-report-file=none", "--disable-warnings", "--no-hints"]

    if disable_verbose:
        pytest_args = [*pytest_args_common, "--tb=short"]
    else:
        pytest_args = [*pytest_args_common, "-vv"]

    # если добавлен флаг -a нет смысла выводить traceback,
    # так как скорее всего задания уже проверены предыдущими запусками.
    if answer:
        pytest_args = [*pytest_args_common, "--tb=no"]

    # запуск pytest
    if tasks == "all":
        pytest.main(pytest_args, plugins=[json_plugin])
    else:
        pytest.main(tasks + pytest_args, plugins=[json_plugin])

    # получить результаты pytest в формате JSON
    passed_tasks = parse_json_report(json_plugin.report)

    # скопировать ответы в файлы answer_task_x.py
    if passed_tasks and answer:
        copy_answers(passed_tasks)


if __name__ == "__main__":
    cli()
