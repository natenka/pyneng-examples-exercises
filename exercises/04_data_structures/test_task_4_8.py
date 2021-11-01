import sys

sys.path.append("..")

from pyneng_common_functions import check_pytest, unified_columns_output

check_pytest(__loader__, __file__)


def test_task_stdout(capsys):
    """
    Проверка работы задания
    """
    import task_4_8

    out, err = capsys.readouterr()
    correct_stdout = unified_columns_output(
        "192       168       3         1\n" "11000000  10101000  00000011  00000001\n"
    )
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert correct_stdout == unified_columns_output(
        out.strip()
    ), "На стандартный поток вывода выводится неправильная строка"
