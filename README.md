# Задания и примеры из книги "Python для сетевых инженеров"

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/) [![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/) [![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Все примеры и задания были проверены на Python 3.7 и 3.8.

## Как создать свой репозиторий для выполнения заданий

> [Подробнее о работе с Git и Github в книге](https://pyneng.readthedocs.io/ru/latest/book/02_git_github/index.html)

### Создание репозитория на GitHub

Для создания своего репозитория на основе шаблона нужно:

-  залогиниться на [GitHub](https://github.com/)
-  открыть [репозиторий с заданиями](https://github.com/natenka/pyneng-examples-exercises)
-  нажать "Use this template" и создать новый репозиторий на основе этого шаблона
-  в открывшемся окне надо ввести название репозитория
-  после этого готов новый репозиторий с копией всех файлов из исходного репозитория с заданиями

![](https://raw.githubusercontent.com/natenka/PyNEng/master/images/git/github_use_template.png)

### Клонирование репозитория с GitHub

Для локальной работы с репозиторием его нужно клонировать.
Для этого используется команда git clone:

```
$ git clone git@github.com:natenka/pyneng-examples-exercises.git
Cloning into 'pyneng-examples-exercises'...
remote: Counting objects: 241, done.
remote: Compressing objects: 100% (191/191), done.
remote: Total 241 (delta 43), reused 239 (delta 41), pack-reused 0
Receiving objects: 100% (241/241), 119.60 KiB | 0 bytes/s, done.
Resolving deltas: 100% (43/43), done.
Checking connectivity... done.
```

По сравнению с приведённой в этом листинге командой, вам нужно изменить:

-  имя пользователя natenka на имя своего пользователя на GitHub;
-  имя репозитория pyneng-examples-exercises на имя своего
   репозитория на GitHub.

В итоге, в текущем каталоге, в котором была выполнена команда git clone,
появится каталог с именем репозитория, в моём случае –
"pyneng-examples-exercises". В этом каталоге теперь находится
содержимое репозитория на GitHub.

## Виртуалки

Для курса подготовлены два варианта виртуальных машин: vmware и Vagrant.
По ссылке есть инструкции для каждого варианта, а также инструкция по выполнению заданий на Windows:

* https://pyneng.github.io/docs/course-vm/


## Задания

В каталоге exercises находятся задания к курсу, отсортированные по разделам курса.
Кроме того, там находятся все вспомогательные файлы (конфигурации и др), которые используются в заданиях.

> Если в заданиях раздела есть задания с буквами (например, 5.2a), то можно выполнить сначала задания без букв, а затем с буквами. Задания с буквами, как правило, немного сложнее заданий без букв и развивают/усложняют идею в соответствующем задании без буквы.
> Например, если в разделе есть задания: 5.1, 5.2, 5.2a, 5.2b, 5.3, 5.3a.
> Сначала, можно выполнить задания 5.1, 5.2, 5.3. А затем 5.2a, 5.2b, 5.3a.
> Однако, если задания с буквами получается сделать сразу, можно делать их по порядку.

## Тесты

Начиная с раздела «9. Функции» для проверки заданий есть автоматические тесты. 
Они помогают проверить все ли соответствует поставленной задаче, а также дают обратный отклик по тому, 
что не соответствует задаче. Как правило, после первого периода адаптации к тестам, становится проще делать задания с тестами.

* [Как работать с тестами и основы pytest](https://pyneng.readthedocs.io/ru/latest/book/additional_info/pytest.html)

Для работы тестов, у вас должны быть установлены дополнительные библиотеки Python.
Если вы работаете в виртуальном окружении, то Вы можете установить все требуюемые библиотеки следующим способом:  
`pip install -r requirements.txt`
