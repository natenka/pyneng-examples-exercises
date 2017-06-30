#Задания

{% include "../exercises_intro.md" %}

### Задание 7.1

Создать функцию, которая генерирует конфигурацию для access-портов.

Параметр access ожидает, как аргумент, словарь access-портов, вида:
```python
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17,
 'FastEthernet0/17':150}
```

Функция должна возвращать список всех портов в режиме access
с конфигурацией на основе шаблона access_template.

В конце строк в списке не должно быть символа перевода строки.

Пример итогового списка:
```python
[
'interface FastEthernet0/12',
'switchport mode access',
'switchport access vlan 10',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
'interface FastEthernet0/17',
'switchport mode access',
'switchport access vlan 150',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
...]
```

Проверить работу функции на примере словаря access_dict.

```python
def generate_access_config(access):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17}
    
    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']


access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }
```

### Задание 7.1a
Сделать копию скрипта задания 7.1.

Дополнить скрипт:
* ввести дополнительный параметр, который контролирует будет ли настроен port-security
 * имя параметра 'psecurity'
 * по умолчанию значение False

Проверить работу функции на примере словаря access_dict,
с генерацией конфигурации port-security и без.

```python
def generate_access_config(access):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17 }
    
    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
        - если значение True, то настройка выполняется с добавлением шаблона port_security
        - если значение False, то настройка не выполняется
    
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """

    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }
```


### Задание 7.1b
Сделать копию скрипта задания 7.1a.

Изменить скрипт таким образом, чтобы функция возвращала не список команд, а словарь:
* ключи: имена интерфейсов, вида 'FastEthernet0/12'
* значения: список команд, который надо выполнить на этом интерфейсе:
```python
      ['switchport mode access',
       'switchport access vlan 10',
       'switchport nonegotiate',
       'spanning-tree portfast',
       'spanning-tree bpduguard enable']
 ```       

Проверить работу функции на примере словаря access_dict,
с генерацией конфигурации port-security и без.

```python
def generate_access_config(access):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17 }
    
    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
        - если значение True, то настройка выполняется с добавлением шаблона port_security
        - если значение False, то настройка не выполняется
    
    Функция возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
    """

    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }
```


### Задание 7.2
Создать функцию, которая генерирует конфигурацию для trunk-портов.

Параметр trunk - это словарь trunk-портов. 

Словарь trunk имеет такой формат (тестовый словарь trunk_dict уже создан):
```python
{ 'FastEthernet0/1':[10,20],
  'FastEthernet0/2':[11,30],
  'FastEthernet0/4':[17] }
```

Функция должна возвращать список команд с конфигурацией на основе указанных портов и шаблона trunk_template.

В конце строк в списке не должно быть символа перевода строки.

Проверить работу функции на примере словаря trunk_dict.

```python
def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов для которых необходимо сгенерировать конфигурацию.
    
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']

trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }
```

### Задание 7.2a
Сделать копию скрипта задания 7.2

Изменить скрипт таким образом, чтобы функция возвращала не список команд, а словарь:
* ключи: имена интерфейсов, вида 'FastEthernet0/1'
* значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_dict.

```python
def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/1':[10,20],
          'FastEthernet0/2':[11,30],
          'FastEthernet0/4':[17] }
    
    Возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
    """
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']

trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }
```

### Задание 7.3
Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:

```python
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}
 ```

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:

```python
 {'FastEthernet0/1':[10,20],
  'FastEthernet0/2':[11,30],
  'FastEthernet0/4':[17]}
```

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

### Задание 7.3a
Сделать копию скрипта задания 7.3.

Дополнить скрипт:
* добавить поддержку конфигурации, когда настройка access-порта выглядит так:

```
interface FastEthernet0/20
  switchport mode access
  duplex auto
```
То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1

Пример словаря:
```python
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/20':1 }
```
Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

### Задание 7.4

Создать функцию, которая обрабатывает конфигурационный файл коммутатора
и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы вначале можно оставлять).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.

```python
ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    """
    ignore_command = False

    for word in ignore:
        if word in command:
            return True
    return ignore_command


def config_to_dict(config):
    """
    config - имя конфигурационного файла коммутатора

    Возвращает словарь:
    - Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
    - Если у команды верхнего уровня есть подкоманды,
      они должны быть в значении у соответствующего ключа, в виде списка (пробелы вначале можно оставлять).
    - Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком
    """
    pass

```

### Задание 7.4a

Задача такая же, как и задании 7.4.
Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности.
При этом, не привязываясь к конкретным разделам.
Она должна быть универсальной, и сработать, если это будут другие разделы.

Теперь:
* если уровня 2, то команды верхнего уровня будут ключами словаря, а команды подуровней - списками;
* если уровня 3, то самый вложенный должен быть списком, а остальные - словарями.

На примере interface Ethernet0/3.100
```python
{'interface Ethernet0/3.100':{
                    'encapsulation dot1Q 100':[],
                    'xconnect 10.2.2.2 12100 encapsulation mpls':
                        ['backup peer 10.4.4.4 14100',
                         'backup delay 1 1']}}
```

```python
ignore = ['duplex', 'alias', 'Current configuration']

def check_ignore(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    
    """
    ignore_command = False

    for word in ignore:
        if word in command:
            ignore_command = True
    return ignore_command


def config_to_dict(config):
    """
    config - имя конфигурационного файла
    """
    pass
```
