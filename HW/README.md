## Как запускать тесты для всех домашек, начиная со второй

### Подготовка к запуску тестов:

1. Научиться получать актуальную версию этого репозитория

   Для начала нужно впервые скачать репозиторий. У вас есть несколько путей:
    - Нажать code -> Download ZIP. Так я делать не рекомендую, но для первого раза норм
    - Научиться пользоваться консольной утилитой git (вот это рекомендую научиться, полезный навык, который пригодится в
      будущем) https://github.com/git-guides/install-git
    - Сделать это через PyCharm. Вам нужен экшен `Get from Version Control`

   Теперь нужно научиться обновлять вашу копию репозитория, если что-то в нем изменилось, например, добавились новые
   тесты. Тут снова несколько путей:
    - Если вы установили утилиту git, то вам надо сделать `git pull` в папке с проектом
    - Если вы открываете проект в PyCharm, то справа сверху будет синий значок `Update Project`. Нажимаете на него и вы
      победили

2. Если у вас не установлены библиотеки argparse и unittest, то их надо установить. 
   Чтобы это проверить вы можете в интерпретаторе попытаться их заимпортить:
```
>>> import argparse
>>> import unittest
```
Если с ошибкой не падает, то все хорошо, иначе загуглите как установить библиотеки для вашей системы

### Как запустить тесты:

Когда у вас есть все необходимое вы готовы перейти к запуску тестов:

1. Заходим в директорию `python_course`
2. Запускаем файл `python_course/HW/tests.py`

```
usage: tests.py [-h] [--easy | --hard] [--src SRC] [--main MAIN] hw

positional arguments:
  hw           hw number

optional arguments:
  -h, --help   show this help message and exit
  --easy       run tests for easy version of hw (used by default)
  --hard       run tests for hard version of hw
  --src SRC    path to the directory with your code
  --main MAIN  name of your main hw file
```

Например, если вы хотите запустить сложные тесты для второго дз, то вам нужно сделать что-то вроде

```
python3 HW/tests.py 2 --hard --src ../my_source_code/hw2/ --main hw2_code.py
```

Возможно вы заходите научиться запускать тесты из PyCharm, но тут все зависит от тогда, что импортировано как
корень проекта и как настроены source директории. Собственно мне лень писать общую инструкцию. Но вы можете
попытаться запустить тесты из PyCharm самостоятельно. Для это в общем случае надо добавить аргументы запуска
в конфигурацию запускаемого файла.

Возможно рано или поздно инструкция тут все же появится :)