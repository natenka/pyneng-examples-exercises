Установить [Virtualbox](https://www.virtualbox.org/wiki/Downloads) и [Vagrant](https://www.vagrantup.com/downloads.html)

Скачать подготовленный образ Vagrant:
https://drive.google.com/open?id=0ByuSz65Dcv1lUHN6TW5RZEsxZzQ


Vagrant и Virtualbox должны находится в каталоге, в пути к которому нет кириллицы.
Подробнее этот аспект описан в [статье](https://habrahabr.ru/post/251529/) в разделе "Предварительная настройка".


Добавить образ в Vagrant:
```
vagrant box add pyneng pyneng.box
vagrant init pyneng
```

Скачать файл [Vagrantfile](https://raw.githubusercontent.com/natenka/PyNEng/master/exercises/vm/Vagrantfile) в текущий каталог.

После этого:
```
vagrant up
```

Виртуальная машина должна запуститься.

В ней есть предустановленный пользователь:
* Username: vagrant
* Password: vagrant


В виртуальной машине должна быть настроена сеть и по IP доступна хостовая система.

В виртуальной машине установлены редакторы: vim и Sublime Text (на рабочем столе есть иконка).

Каталоги с примерами и упражнениями находятся в каталоге pyneng_files на рабочем столе.

Все модули, которые нужны в курсе, установлены в виртуальном окружении pyneng:
```
workon pyneng
```

