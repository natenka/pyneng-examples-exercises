import re
import sys

import pytest

sys.path.append("..")

from pyneng_common_functions import check_pytest

check_pytest(__loader__, __file__)


def unified_columns_output(output):
    lines = sorted(
        [re.split(r"  +", line.strip()) for line in output.strip().split("\n")]
    )
    formatted = [("{:25}" * len(line)).format(*line) for line in lines]
    return "\n".join(formatted)


@pytest.mark.parametrize(
    "vlan,result",
    [
        (
            "10",
            "10       0a1b.1c80.7000      Gi0/4\n10       01ab.c5d0.70d0      Gi0/8",
        ),
        (
            "1000",
            "1000     0a4b.c380.7d00      Gi0/9",
        ),
    ],
    ids=["vlan 10", "vlan 1000"],
)
def test_task_stdout(capsys, monkeypatch, vlan, result):
    """
    Проверка работы задания
    """
    monkeypatch.setattr("builtins.input", lambda x=None: vlan)
    if sys.modules.get("task_7_3b"):
        del sys.modules["task_7_3b"]
    import task_7_3b

    out, err = capsys.readouterr()
    correct_stdout = unified_columns_output(result)
    assert correct_stdout == unified_columns_output(
        out.strip()
    ), "На стандартный поток вывода выводится неправильная строка"
