# Задания

{% include "../exercises_intro.md" %}

### Задание 8.1

Создать отдельный файл my_func.py.

Перенести в него функции из заданий:
* 7.1 или 7.1a
* 7.2
* 7.3 или 7.3a

Создать файл main.py:
* По ходу задания импортировать нужные функции из файла my_func.
* Файл main.py должен ожидать как аргумент имя конфигурационного файла коммутатора.
* Имя конфигурационного файла передать как аргумент функции get_int_vlan_map (из задания 7.3-7.3a)
 * На выходе функции, мы должны получить кортеж двух словарей.
* Словари, соответственно, надо передать функциям:
 * generate_access_config (из задания 7.1-7.1a)
 * generate_trunk_config (из задания 7.2)
* Эти функции, в свою очередь, возвращают список со строками готовой конфигурации
которую надо записать в файл result.txt в виде стандартного конфига (то есть, строк)

### Задание 8.2

Создать функцию parse_cdp_neighbors, которая обрабатывает
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
{('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
('R4', 'Fa0/2'): ('R6', 'Fa0/0')}
```

Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt


### Задание 8.2a

> Для выполнения этого задания, должен быть установлен graphviz:

> ```apt-get install graphviz```

> И модуль python для работы с graphviz:

> ```pip install graphviz```

С помощью функции parse_cdp_neighbors из задания 8.2
и функции draw_topology из файла draw_network_graph.py,
сгенерировать топологию, которая соответствует выводу
команды sh cdp neighbor в файле sw1_sh_cdp_neighbors.txt

Не копировать код функций parse_cdp_neighbors и draw_topology.

В итоге, должен быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_8_2a_topology.svg

![task_8_2a_topology](https://raw.githubusercontent.com/natenka/PyNEng/master/images/08_modules/task_8_2a_topology.png)



### Задание 8.2b

> Для выполнения этого задания, должен быть установлен graphviz:

> ```apt-get install graphviz```

> И модуль python для работы с graphviz:

> ```pip install graphviz```

С помощью функции parse_cdp_neighbors из задания 8.2
и функции draw_topology из файла draw_network_graph.py,
сгенерировать топологию, которая соответствует выводу
команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt


Не копировать код функций parse_cdp_neighbors и draw_topology.

В итоге, должен быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_8_2b_topology.svg

![task_8_2b_topology](https://raw.githubusercontent.com/natenka/PyNEng/master/images/08_modules/task_8_2b_topology.png)
