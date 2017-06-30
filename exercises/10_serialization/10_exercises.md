# Задания

{% include "../exercises_intro.md" %}

### Задание 10.1

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает аргумент output в котором находится вывод команды sh version
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

Функция write_to_csv:
* ожидает два аргумента:
 * имя файла, в который будет записана информация в формате CSV
 * данные в виде списка списков, где:
    * первый список - заголовки столбцов,
    * остальные списки - содержимое
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает

Остальное содержимое скрипта может быть в скрипте, а может быть в ещё одной функции.

Скрипт должен:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в файл routers_inventory.csv

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
Вы можете раскомментировать строку print sh_version_files, чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.

```python
import glob

sh_version_files = glob.glob('sh_vers*')
#print sh_version_files

headers = ['hostname', 'ios', 'image', 'uptime']

```


### Задание 10.2

Создать функции:
* generate_access_config - генерирует конфигурацию для access-портов, на основе словарей access и psecurity из файла sw_templates.yaml
* generate_trunk_config - генерирует конфигурацию для trunk-портов, на основе словаря trunk из файла sw_templates.yaml
* generate_mngmt_config - генерирует конфигурацию менеджмент настроек, на основе словаря mngmt из файла templates.yaml
* generate_ospf_config - генерирует конфигурацию ospf, на основе словаря ospf из файла templates.yaml
* generate_alias_config - генерирует конфигурацию alias, на основе словаря alias из файла templates.yaml
* generate_switch_config - генерирует конфигурацию коммутатора, в зависимости от переданных параметров, использует для этого остальные функции

```python
import yaml


access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }

trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }


def generate_access_config(access, psecurity=False):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17}
    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
        - если значение True, то настройка выполняется с добавлением шаблона port_security
        - если значение False, то настройка не выполняется

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    pass

def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/1':[10,20],
          'FastEthernet0/2':[11,30],
          'FastEthernet0/4':[17] }

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    pass

def generate_ospf_config(filename):
    """
    filename - имя файла в формате YAML, в котором находится шаблон ospf.

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    templates = yaml.load(open(filename))


def generate_mngmt_config(filename):
    """
    filename - имя файла в формате YAML, в котором находится шаблон mngmt.

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    pass

def generate_alias_config(filename):
    """
    filename - имя файла в формате YAML, в котором находится шаблон alias.

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    pass

def generate_switch_config(access=True, psecurity=False, trunk=True,
                           ospf=True, mngmt=True, alias=False):
    """
    Аргументы контролируют какие настройки надо выполнить.
    По умолчанию, будет настроено все, кроме psecurity и alias.

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    pass

# Сгенерировать конфигурации для разных коммутаторов:

sw1 = generate_switch_config()
sw2 = generate_switch_config(psecurity=True, alias=True)
sw3 = generate_switch_config(ospf=False)

```


### Задание 10.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
```
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0
```

Функция должна вернуть такой словарь:
```python
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}}}
```

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

### Задание 10.3a

С помощью функции parse_sh_cdp_neighbors из задания 10.3,
обработать вывод команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Объединить все словари, которые возвращает функция parse_sh_cdp_neighbors,
в один словарь topology и записать его содержимое в файл topology.yaml.

Структура словаря topology должна быть такой:
```python
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}},
 'R5': {'Fa0/1': {'R4': 'Fa0/1'}},
 'R6': {'Fa0/0': {'R4': 'Fa0/2'}}}
```

Не копировать код функции parse_sh_cdp_neighbors


### Задание 10.3b

Переделать функциональность скрипта из задания 10.3a,
в функцию generate_topology_from_cdp.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_file - этот параметр управляет тем, будет ли записан в файл, итоговый словарь
 * значение по умолчанию - True
* topology_filename - имя файла, в который сохранится топология.
 * по умолчанию, должно использоваться имя topology.yaml.
 * топология сохраняется только, если аргумент save_to_file указан равным True

Функция возвращает словарь, который описывает топологию.
Словарь должен быть в том же формате, что и в задании 10.3a.

Проверить работу функции generate_topology_from_cdp на файлах:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Записать полученный словарь в файл topology.yaml.

Не копировать код функции parse_sh_cdp_neighbors


### Задание 10.3c

С помощью функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует описанию в файле topology.yaml

Обратите внимание на то, какой формат данных ожидает функция draw_topology.
Описание топологии из файла topology.yaml нужно преобразовать соответствующим образом,
чтобы использовать функцию draw_topology.

Для решения задания можно создать любые вспомогательные функции.

В итоге, должно быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_10_3c_topology.svg

Не копировать код функции draw_topology.

> Для выполнения этого задания, должен быть установлен graphviz:
> ```pip install graphviz```

![task_10_3c_topology](https://raw.githubusercontent.com/natenka/PyNEng/master/images/10_serialization/task_10_3c_topology.png)

