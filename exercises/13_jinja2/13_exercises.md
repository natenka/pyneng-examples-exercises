# Задания

{% include "../exercises_intro.md" %}

### Задание 13.1

Переделать скрипт cfg_gen.py в функцию generate_cfg_from_template.

Функция ожидает два аргумента:
* путь к шаблону
* файл с переменными в формате YAML

Функция должна возвращать конфигурацию, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt и данных data_files/for.yml.

```python
from jinja2 import Environment, FileSystemLoader
import yaml
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

TEMPLATE_DIR, template = sys.argv[1].split('/')
VARS_FILE = sys.argv[2]

env = Environment(loader = FileSystemLoader(TEMPLATE_DIR), trim_blocks=True)
template = env.get_template(template)

vars_dict = yaml.load( open( VARS_FILE ) )

print template.render( vars_dict )
```

### Задание 13.1a

Переделать функцию generate_cfg_from_template:
* добавить поддержку использования шаблона, который находится в текущем каталоге

Для проверки, скопируйте один из шаблонов из каталога templates,
в текущий каталог скрипта.

Можно проверить на тех же шаблоне и данных, что и в прошлом задании:
* шаблоне templates/for.txt (но скопировать его в текущий каталог) и данных data_files/for.yml


### Задание 13.1b

Дополнить функцию generate_cfg_from_template из задания 13.1 или 13.1a:
* добавить поддержку аргументов окружения (Environment)

Функция generate_cfg_from_template должна принимать любые аргументы,
которые принимает класс Environment и просто передавать их ему.

Проверить функциональность на аргументах:
* trim_blocks
* lstrip_blocks


### Задание 13.1c

Дополнить функцию generate_cfg_from_template из задания 13.1, 13.1a или 13.1b:
* добавить поддержку разных форматов для файла с данными

Должны поддерживаться такие форматы:
* YAML
* JSON
* словарь Python

Сделать для каждого формата свой параметр функции.
Например:
* YAML - yaml_file
* JSON - json_file
* словарь Python - py_dict

Проверить работу функции на шаблоне templates/for.txt и данных:
* data_files/for.yml
* data_files/for.json
* словаре data_dict

```python
data_dict = {'vlans': {
                        10: 'Marketing',
                        20: 'Voice',
                        30: 'Management'},
             'ospf': [{'network': '10.0.1.0 0.0.0.255', 'area': 0},
                      {'network': '10.0.2.0 0.0.0.255', 'area': 2},
                      {'network': '10.1.1.0 0.0.0.255', 'area': 0}],
             'id': 3,
             'name': 'R3'}
```


### Задание 13.1d

Переделать функцию generate_cfg_from_template из задания 13.1, 13.1a, 13.1b или 13.1c:
* сделать автоматическое распознавание разных форматов для файла с данными
* для передачи разных типов данных, должен использоваться один и тот же параметр data

Должны поддерживаться такие форматы:
* YAML - файлы с расширением yml или yaml
* JSON - файлы с расширением json
* словарь Python

Если не получилось определить тип данных, вывести сообщение error_message (перенести текст сообщения в тело функции), завершить работу функции и вернуть ```None```.

Проверить работу функции на шаблоне templates/for.txt и данных:
* data_files/for.yml
* data_files/for.json
* словаре data_dict

```python
error_message = """
Не получилось определить формат данных.
Поддерживаются файлы с расширением .json, .yml, .yaml и словари Python
"""

data_dict = {'vlans': {
                        10: 'Marketing',
                        20: 'Voice',
                        30: 'Management'},
             'ospf': [{'network': '10.0.1.0 0.0.0.255', 'area': 0},
                      {'network': '10.0.2.0 0.0.0.255', 'area': 2},
                      {'network': '10.1.1.0 0.0.0.255', 'area': 0}],
             'id': 3,
             'name': 'R3'}
```


### Задание 13.2

На основе конфигурации config_r1.txt, создать шаблоны:
* templates/cisco_base.txt - в нем должны быть все строки, кроме настройки alias и event manager
 * имя хоста должно быть переменной hostname
* templates/alias.txt - в этот шаблон перенести все alias
* templates/eem_int_desc.txt - в этом шаблоне должен быть event manager applet

В шаблонах templates/alias.txt и templates/eem_int_desc.txt переменных нет.

Создать шаблон templates/cisco_router_base.txt.
В шаблон должно быть включено содержимое шаблонов:
* templates/cisco_base.txt
* templates/alias.txt
* templates/eem_int_desc.txt

При этом, нельзя копировать текст шаблонов.

Проверьте шаблон templates/cisco_router_base.txt,
с помощью функции generate_cfg_from_template из задания 13.1-13.1d.
Не копируйте код функции.

В качестве данных, используйте словарь router_info

```python
router_info = { 'hostname': 'R1' }
```

### Задание 13.3

Создайте шаблон templates/ospf.txt на основе конфигурации OSPF в файле cisco_ospf.txt.
Пример конфигурации дан, чтобы напомнить синтаксис.

Какие значения должны быть переменными:
* номер процесса. Имя переменной - ```process```
* router-id. Имя переменной - ```router_id```
* reference-bandwidth. Имя переменной - ```ref_bw```
* интерфейсы, на которых нужно включить OSPF. Имя переменной - ```ospf_intf```
 * на месте этой переменной ожидается список словарей с такими ключами:
  * ```name``` - имя интерфейса, вида Fa0/1, VLan10, Gi0/0
  * ```ip``` - IP-адрес интерфейса, вида 10.0.1.1
  * ```area``` - номер зоны
  * ```passive``` - является ли интерфейс пассивным. Допустимые значения: True или False

Для всех интерфейсов в списке ospf_intf, надо сгенерировать строки:
```
 network x.x.x.x 0.0.0.0 area x
```

Если интерфейс пассивный, для него должна быть добавлена строка:
```
 passive-interface x
```

Для интерфейсов, которые не являются пассивными, в режиме конфигурации интерфейса,
надо добавить строку:
```
 ip ospf hello-interval 1
```


Все команды должны быть в соответствующих режимах.

Проверьте получившийся шаблон templates/ospf.txt, на данных в файле data_files/ospf.yml,
с помощью функции generate_cfg_from_template из задания 13.1-13.1d.
Не копируйте код функции.

### Задание 13.3a

Измените шаблон templates/ospf.txt таким образом, чтобы для перечисленных переменных
были указаны значения по умолчанию, которые используются в том случае,
если переменная не задана.

Не использовать для этого выражения if/else.

Задать в шаблоне значения по умолчанию для таких переменных:
* process - значение по умолчанию 1
* ref_bw - значение по умолчанию 10000


Проверьте получившийся шаблон templates/ospf.txt, на данных в файле data_files/ospf2.yml,
с помощью функции generate_cfg_from_template из задания 13.1-13.1d.
Не копируйте код функции.


### Задание 13.3b

Измените шаблон templates/ospf.txt из задания 13.3a таким образом,
чтобы для перечисленных переменных были указаны значения по умолчанию,
которые используются в том случае, если переменная не задана или,
если в переменной пустое значение.

Не использовать для этого выражения if/else.

Задать в шаблоне значения по умолчанию для таких переменных:
* process - значение по умолчанию 1
* ref_bw - значение по умолчанию 10000


Проверьте получившийся шаблон templates/ospf.txt, на данных в файле data_files/ospf3.yml,
с помощью функции generate_cfg_from_template из задания 13.1-13.1d.
Не копируйте код функции.

### Задание 13.4

Создайте шаблон templates/add_vlan_to_switch.txt, который будет использоваться
при необходимости добавить VLAN на коммутатор.

В шаблоне должны поддерживаться возможности:
* добавления VLAN и имени VLAN
* добавления VLAN как access, на указанном интерфейсе
* добавления VLAN в список разрешенных, на указанные транки

Если VLAN необходимо добавить как access,
то надо настроить и режим интерфейса и добавить его в VLAN:
```
interface Gi0/1
 switchport mode access
 switchport access vlan 5
```

Для транков, необходимо только добавить VLAN в список разрешенных:
```
interface Gi0/10
 switchport trunk allowed vlan add 5
```

Имена переменных надо выбрать на основании примера данных,
в файле data_files/add_vlan_to_switch.yaml.


Проверьте шаблон templates/add_vlan_to_switch.txt
на данных в файле data_files/add_vlan_to_switch.yaml,
с помощью функции generate_cfg_from_template из задания 13.1-13.1d.
Не копируйте код функции.

