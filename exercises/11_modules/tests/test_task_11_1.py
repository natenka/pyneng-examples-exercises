import pytest
import task_11_1
import sys
sys.path.append('..')

from common_functions import check_function_exists, check_function_params


def test_function_created():
    check_function_exists(task_11_1, 'parse_cdp_neighbors')


def test_function_params():
    check_function_params(function=task_11_1.parse_cdp_neighbors,
                          param_count=1, param_names=['command_output'])


def test_argument_type():
    sh_cdp_n_sw1 = (
        'SW1>show cdp neighbors\n\n'
        'Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge\n'
        '                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone\n\n'
        'Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID\n'
        'R1           Eth 0/1         122           R S I           2811       Eth 0/0\n'
        'R2           Eth 0/2         143           R S I           2811       Eth 0/0\n'
        'R3           Eth 0/3         151           R S I           2811       Eth 0/0\n'
        'R6           Eth 0/5         121           R S I           2811       Eth 0/1')
    try:
        return_value = task_11_1.parse_cdp_neighbors(sh_cdp_n_sw1)
    except OSError as err:
        if 'File name too long' in ''.join(map(str, err.args)):
            pytest.fail("Функция должна ожидать как аргумент вывод команды одной строкой, а не имя файла")


def test_function_return_value():
    sh_cdp_n_sw1 = (
        'SW1>show cdp neighbors\n\n'
        'Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge\n'
        '                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone\n\n'
        'Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID\n'
        'R1           Eth 0/1         122           R S I           2811       Eth 0/0\n'
        'R2           Eth 0/2         143           R S I           2811       Eth 0/0\n'
        'R3           Eth 0/3         151           R S I           2811       Eth 0/0\n'
        'R6           Eth 0/5         121           R S I           2811       Eth 0/1')
    correct_return_value = {('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                            ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                            ('SW1', 'Eth0/3'): ('R3', 'Eth0/0'),
                            ('SW1', 'Eth0/5'): ('R6', 'Eth0/1')}

    return_value = task_11_1.parse_cdp_neighbors(sh_cdp_n_sw1)
    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == dict, "Функция должна возвращать словарь"
    assert return_value == correct_return_value, "Функция возвращает неправильное значение"

