import pytest
import task_15_3
import sys
sys.path.append('..')

from common_functions import check_function_exists


def test_function_created():
    check_function_exists(task_15_3, 'convert_ios_nat_to_asa')


def test_function_return_value(tmpdir):
    asa_nat_config = (
        'object network LOCAL_10.66.0.13\n'
        ' host 10.66.0.13\n'
        ' nat (inside,outside) static interface service tcp 995 995\n'
        'object network LOCAL_10.66.0.21\n'
        ' host 10.66.0.21\n'
        ' nat (inside,outside) static interface service tcp 20065 20065\n'
        'object network LOCAL_10.66.0.22\n'
        ' host 10.66.0.22\n'
        ' nat (inside,outside) static interface service tcp 443 44443\n'
        'object network LOCAL_10.66.0.23\n'
        ' host 10.66.0.23\n'
        ' nat (inside,outside) static interface service tcp 2565 2565\n'
        'object network LOCAL_10.1.2.28\n'
        ' host 10.1.2.28\n'
        ' nat (inside,outside) static interface service tcp 563 563\n'
        'object network LOCAL_10.98.1.1\n'
        ' host 10.98.1.1\n'
        ' nat (inside,outside) static interface service tcp 3389 3389\n'
        'object network LOCAL_10.14.1.15\n'
        ' host 10.14.1.15\n'
        ' nat (inside,outside) static interface service tcp 12220 12220\n'
        'object network LOCAL_10.14.1.169\n'
        ' host 10.14.1.169\n'
        ' nat (inside,outside) static interface service tcp 25565 25565\n'
        'object network LOCAL_10.66.0.26\n'
        ' host 10.66.0.26\n'
        ' nat (inside,outside) static interface service tcp 220 220\n'
        'object network LOCAL_10.66.37.11\n'
        ' host 10.66.37.11\n'
        ' nat (inside,outside) static interface service tcp 80 8080\n'
        'object network LOCAL_10.66.37.13\n'
        ' host 10.66.37.13\n'
        ' nat (inside,outside) static interface service tcp 10995 10995\n'
        'object network LOCAL_10.1.2.84\n'
        ' host 10.1.2.84\n'
        ' nat (inside,outside) static interface service tcp 22 20022\n'
        'object network LOCAL_10.1.2.66\n'
        ' host 10.1.2.66\n'
        ' nat (inside,outside) static interface service tcp 22 20023\n'
        'object network LOCAL_10.1.2.63\n'
        ' host 10.1.2.63\n'
        ' nat (inside,outside) static interface service tcp 80 80\n'
    )
    dest_filename = tmpdir.mkdir("test_tasks").join("task_15_3.txt")
    return_value = task_15_3.convert_ios_nat_to_asa('cisco_nat_config.txt',
                                                    dest_filename)
    assert return_value == None, "Функция должна возвращать None"
    assert dest_filename.read().strip() == asa_nat_config.strip(),\
            "Неправильная конфигурация для ASA"

