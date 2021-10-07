### Подготовка к запуску тестов:

1. Склонить себе этот репозиторий ... Тут надо ссылки как это сделать
2. Установить либы (argparse и unittest - мб дефолтная) ... Тоже надо ссылки как установить

### Как запустить тесты:

1. Заходим в директорию `python_course` или `python_course/HW` (далее примеры для `python_course`)
2. Запускаем файл `python_course/HW/tests.py`

```
usage: tests.py [-h] [--easy | --hard] [--src SRC] [--main MAIN] hw

positional arguments:
  hw           hw number

optional arguments:
  -h, --help   show this help message and exit
  --easy       run tests for easy version of hw (use by default)
  --hard       run tests for hard version of hw
  --src SRC    path to the directory with your code
  --main MAIN  name of your main hw file
```

Например, если вы хотите запустить сложные тесты для второго дз, то вам нужно сделать что-то вроде

```
python3 HW/tests.py 2 --hard --src ../my_source_code/hw2/ --main hw2_code.py
```

При запусках из PyCharm могут быть нюансы: все зависит от того, что импортировано как корень проекта и как настроены src
директории. Но в общем случае надо добавить параметры в конфиг запуска