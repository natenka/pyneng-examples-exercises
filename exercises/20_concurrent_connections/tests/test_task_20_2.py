import pytest
import task_20_2
import sys
sys.path.append('..')

from common_functions import check_function_exists



def test_functions_created():
    check_function_exists(task_20_2, 'send_show_command_to_devices')


def test_function_return_value(three_routers_from_devices_yaml,
                               r1_r2_r3_test_connection, tmpdir):
    command = 'sh ip int br'
    out1, out2, out3 = [r.send_command(command) for r in r1_r2_r3_test_connection]
    dest_filename = tmpdir.mkdir("test_tasks").join("task_20_2.txt")

    return_value = task_20_2.send_show_command_to_devices(
        devices=three_routers_from_devices_yaml,
        command=command, filename=dest_filename, limit=3)
    assert return_value == None, "Функция должна возвращать None"

    dest_file_content = dest_filename.read().strip()

    # проверяем, что вывод с каждого устройства есть в файле
    assert out1.strip() in dest_file_content, "В итоговом файле нет вывода с первого устройства"
    assert out2.strip() in dest_file_content, "В итоговом файле нет вывода со второго устройства"
    assert out3.strip() in dest_file_content, "В итоговом файле нет вывода с третьего устройства"
