Установить [Virtualbox](https://www.virtualbox.org/wiki/Downloads) и [Vagrant](https://www.vagrantup.com/downloads.html)

Скачать [подготовленный образ Vagrant](https://drive.google.com/open?id=0ByuSz65Dcv1leGw5VzhscXA5Ymc)

> [Эта же инструкция в видео формате](https://drive.google.com/open?id=0B0NXr5fFaEWCT1VCSkhhaVlVRG8).

Vagrant и Virtualbox должны находится в каталоге, в пути к которому нет кириллицы.
Подробнее этот аспект описан в [статье](https://habrahabr.ru/post/251529/) в разделе "Предварительная настройка".

> Для работы Vagrant в Windows требуется PowerShell >= 3 версии. В Windows 7 из-за этого возникали проблемы. 
> После обновления PowerShell, первый раз нужно выполнить ```vagrant up``` внутри PowerShell. В следующий раз, можно запускать уже из командной строки.

Добавить образ в Vagrant (при условии, что файл pyneng-py3.box находится в текущем каталоге):
```
vagrant box add pyneng pyneng-py3.box
vagrant init pyneng
```
После этого в текущем каталоге создался файл Vagrantfile.

В нем необходимо раскомментировать несколько строк.
Найдите соответствующую секцию в  файле и удалите символ решетки перед строками, как в выводе:
```
  config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
    vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
     vb.memory = "1024"

  end
```

> Объем памяти можно указать любым.

После этого:
```
vagrant up
```

Виртуальная машина должна запуститься.

В ней есть предустановленный пользователь:

* Username: vagrant
* Password: vagrant


В виртуальной машине:

* настроена сеть и по IP доступна хостовая система.
* установлены редакторы: vim и Sublime Text (на рабочем столе есть иконка).


Все модули, которые нужны в курсе, установлены в [виртуальном окружении](https://natenka.gitbooks.io/pyneng/content/v/python3.6/book/01_intro/virtualenv.html) pyneng-py3.
Перейти в него можно с помощью команды:
```
workon pyneng-py3
```
