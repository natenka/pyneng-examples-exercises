# Задания

{% include "../exercises_intro.md" %}

### Задание 4.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

```
Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
```

Проверить работу скрипта на разных комбинациях сеть/маска.


### Задание 4.1a

Всё, как в задании 4.1. Но, если пользователь ввел адрес хоста, а не адрес сети, то надо адрес хоста преобразовать в адрес сети и вывести адрес сети и маску, как в задании 4.1.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

```
Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
```

Проверить работу скрипта на разных комбинациях сеть/маска.


### Задание 4.1b

Преобразовать скрипт из задания 4.1a таким образом, чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту. 


### Задание 4.2

В этой задаче нельзя использовать условие if и нельзя изменять словарь london_co.

В задании создан словарь с информацией о разных устройствах.

Вам нужно запросить у пользователя ввод имени устройства (r1, r2 или sw1).
И вывести информацию о соответствующем устройстве на стандартный поток вывода
(информация будет в виде словаря).


Пример выполнения скрипта:
```
$ python task_4_2.py
Enter device name: r1
{'ios': '15.4', 'model': '4451', 'vendor': 'Cisco', 'location': '21 New Globe Walk', 'ip': '10.255.0.1'}
```


```python
london_co = {
    'r1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.1'
    },
    'r2' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.2'
    },
    'sw1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '3850',
    'ios': '3.6.XE',
    'ip': '10.255.0.101',
    'vlans': '10,20,30',
    'routing': True
    }
}
```

### Задание 4.2a

В этой задаче нельзя использовать условие if и нельзя изменять словарь london_co.

Переделать скрипт из задания 4.2 таким образом, чтобы,
кроме имени устройства, запрашивался также параметр устройства, который нужно отобразить.

Вывести информацию о соответствующем параметре, указанного устройства.

Пример выполнения скрипта:
```
$ python task_4_2a.py
Enter device name: r1
Enter parameter name: ios
15.4
```

```python
london_co = {
    'r1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.1'
    },
    'r2' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.2'
    },
    'sw1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '3850',
    'ios': '3.6.XE',
    'ip': '10.255.0.101',
    'vlans': '10,20,30',
    'routing': True
    }
}
```

### Задание 4.2b

В этой задаче нельзя использовать условие if и нельзя изменять словарь london_co.

Переделать скрипт из задания 4.2a таким образом, чтобы, при запросе параметра,
отображался список возможных параметров.

Вывести информацию о соответствующем параметре, указанного устройства.

Пример выполнения скрипта:
```
$ python task_4_2b.py
Enter device name: r1
Enter parameter name (ios,model,vendor,location,ip): ip
10.255.0.1
```

```python
london_co = {
    'r1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.1'
    },
    'r2' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.2'
    },
    'sw1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '3850',
    'ios': '3.6.XE',
    'ip': '10.255.0.101',
    'vlans': '10,20,30',
    'routing': True
    }
}
```


### Задание 4.2c

В этой задаче нельзя использовать условие if и нельзя изменять словарь london_co.

Переделать скрипт из задания 4.2b таким образом, чтобы, при запросе параметра,
которого нет в словаре устройства, отображалось сообщение 'Такого параметра нет'.

> Попробуйте набрать неправильное име параметра или несуществующий параметр, чтобы увидеть какой будет результат. А затем выполняйте задание.

Если выбран существующий параметр,
вывести информацию о соответствующем параметре, указанного устройства.

Пример выполнения скрипта:
```
$ python task_4_2c.py
Enter device name: r1
Enter parameter name (ios,model,vendor,location,ip): io
Такого параметра нет
```

```python
london_co = {
    'r1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.1'
    },
    'r2' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.2'
    },
    'sw1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '3850',
    'ios': '3.6.XE',
    'ip': '10.255.0.101',
    'vlans': '10,20,30',
    'routing': True
    }
}
```


### Задание 4.2d

В этой задаче нельзя использовать условие if и нельзя изменять словарь london_co.

Переделать скрипт из задания 4.2c таким образом, чтобы, при запросе параметра,
пользователь мог вводить название параметра в любом регистре.

Пример выполнения скрипта:
```
$ python task_4_2d.py
Enter device name: r1
Enter parameter name (ios,model,vendor,location,ip): IOS
15.4
```

```python
london_co = {
    'r1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.1'
    },
    'r2' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.2'
    },
    'sw1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '3850',
    'ios': '3.6.XE',
    'ip': '10.255.0.101',
    'vlans': '10,20,30',
    'routing': True
    }
}
```


### Задание 4.3

(Задача на основе примеров в разделе)

В этой задаче нельзя использовать условие if.

Скрипт должен запрашивать у пользователя:
* информацию о режиме интерфейса (access/trunk),
  * пример текста запроса: 'Enter interface mode (access/trunk): '
* номере интерфейса (тип и номер, вида Gi0/3)
  * пример текста запроса: 'Enter interface type and number: '
* номер VLANа (для режима trunk будет вводиться список VLANов)
  * пример текста запроса: 'Enter vlan(s): '

В зависимости от выбранного режима, на стандартный поток вывода,
должна возвращаться соответствующая конфигурация access или trunk
(шаблоны команд находятся в списках access_template и trunk_template).

При этом, сначала должна идти строка interface и подставлен номер интерфейса,
а затем соответствующий шаблон, в который подставлен номер VLANа (или список VLANов).


Ниже примеры выполнения скрипта, чтобы было проще понять задачу.

Пример выполнения скрипта, при выборе режима access:
```
$ python task_4_3.py
Enter interface mode (access/trunk): access
Enter interface type and number: Fa0/6
Enter vlan(s): 3

interface Fa0/6
switchport mode access
switchport access vlan 3
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
```

Пример выполнения скрипта, при выборе режима trunk:
```
$ python task_4_3.py
Enter interface mode (access/trunk): trunk
Enter interface type and number: Fa0/7
Enter vlan(s): 2,3,4,5

interface Fa0/7
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 2,3,4,5
```

Начальное содержимое скрипта:
```python
access_template = ['switchport mode access',
                   'switchport access vlan %s',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan %s']

```


### Задание 4.3a

В этой задаче нельзя использовать условие if.

Дополнить скрипт из задания 4.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'

```python
access_template = ['switchport mode access',
                   'switchport access vlan %s',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan %s']

```
