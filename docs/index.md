# Программирование

## Домашние задания

При выполнении более сложной версии необходимо выполнение и всех предыдущих уровней сложности.

### 1. Сумма чисел 
* #### Basic 
   
    Получить сумму чисел, вводящихся на консоль, до появления первого 0.
    
    _Примеры_:

    | Ввод       | Вывод               |
    | ------------- |:------------------:|
    | 1<br>2<br>3<br>0| 6    |
    | 1<br>-2<br>3<br>0    | 2 |

* #### Medium 
    
    Вывести сумму всех чисел, всех только положительных и только отрицательных отдельно
    
    _Примеры_:

    | Ввод       | Вывод               |
    | ------------- |:------------------:|
    | 1<br>2<br>3<br>0| 6 6 0   |
    | 1<br>-2<br>3<br>0    | 2 4 -2 |
* #### Hard
    
    На вход могут приходить не только числа
    
    _Примеры_:

    | Ввод       | Вывод               |
    | ------------- |:------------------:|
    | 1<br>2<br>3<br>0| 6 6 0   |
    | 1<br>-2<br>3<br>0    | 2 4 -2 |
    | 1<br>hello<br>3<br>0    | 4 4 0 |
    | 1<br>-2<br>hello<br>3<br>0    | 2 4 -2 |

### 2. Функции! Функции! Функции!
* #### Basic 
   
    1. Функция Аккермана
  
        Написать свою реализацию `ackermann`[функции Аккермана](https://math.wikia.org/ru/wiki/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D1%8F_%D0%90%D0%BA%D0%BA%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B0)
        
        _Примеры_:
  
        | Ввод       | Вывод               |
        | ------------- |:------------------:|
        | 0 0| 1    |
        | 1 2    | 4 |
    2. Generate count
       
       Написать функцию `generate_count`, возвращающую функцию, которая при каждом новом вызове возвращает значение, увеличенное на 1.
       
       Изначальное значение счетчика можно передать в `generate_count`
  
       _Ожидаемое поведение_:
       
       ```python
          counter = generate_counter()
          print(counter()) # 1
          print(counter()) # 2
       ```
    
       ```python
          counter = generate_counter(5)
          print(counter()) # 6
          print(counter()) # 7
       ```

* #### Hard
    
    1. Странные суммы
       
       Написать функцию `sum` со следующей семантикой:
  
       _Ожидаемое поведение_:
       
       ```python
          sum(1)(2)(-1)(3)() # 5
          sum() # 0
       ```
       
    2. Частичное применение
  
        Написать свою функцию для частичного применения `part`
  
        _Ожидаемое поведение_:
       
       ```python
          def mul(a, b, c):
              return a * b * c

          mul1 = part(mul, 1)
          print(mul1(2, 3))  # 6
          mul2 = part(mul, 1, 2)
          print(mul2(5))  # 10
          mul3 = part(mul, 1, 2, -3)
          print(mul3())  # -6
       ```

### 3. Коллектор
* #### Basic 
   
   1. Разработайте функцию, которая будет подсчитывать статистику встречаемости слов во входном файле.
   2. Словом называется непрерывная последовательность букв, апострофов и тире (Unicode category Punctuation, Dash). Для подсчета статистики, слова приводятся к нижнему регистру.
   3. Имена входного и выходного файла задаются в качестве аргументов к функции
   4. Программа должна работать за линейное от размера входного файла время.
   5. Выходной файл должен содержать все различные слова, встречающиеся во входном файле, в порядке их появления. Для каждого слова должна быть выведена одна строка, содержащая слово и число его вхождений во входной файл

* #### Hard
   6. и номера вхождений этого слова среди всех слов во входном файле
   7. Также разработайте приложение, где файлы - аргументы командной строки 

   Как получить аргументы командной строки:
   ```python
   # main.py
   import sys

   if __name__ == "__main__":
      print("Arguments count:", str(len(sys.argv))) 
      # sys.argv - массив строк с аргументами командной строки
      for arg in sys.argv:
         print(arg)
   ```

   Запуск:
   ```bash
   python3 your_program.py <input.txt> <output.txt> 
   ```
   _Примеры_:

   _Easy_:

   | Вводной файл       | Выводной файл               |
   | ------------- |:------------------:|
   | To be, or not to be, that is the question: | to 2<br> be 2<br> or 1<br> not 1<br> that 1<br> is 1<br> the 1<br> question 1|
   | Шалтай-Болтай <br> Сидел на стене. <br> Шалтай-Болтай <br> Свалился во сне. | шалтай-болтай 2 <br> сидел 1<br> на 1<br> стене 1<br> свалился 1<br> во 1<br> сне 1|

   _Hard_:

   | Вводной файл       | Выводной файл               |
   | ------------- |:------------------:|
   | To be, or not to be, that is the question: | to 2 1 5 <br> be 2 2 6 <br> or 1 3 <br> not 1 4 <br> that 1 7 <br> is 1 8 <br> the 1 9 <br> question 1 10|
   | Шалтай-Болтай <br> Сидел на стене. <br> Шалтай-Болтай <br> Свалился во сне. | шалтай-болтай 2 1 5 <br> сидел 1 2 <br> на 1 3 <br> стене 1 4 <br> свалился 1 6 <br> во 1 7 <br> сне 1 8 |


### 4. Я тебя по ip вычислю! 
* #### Universal

   По заданному списку ip адресов необходимо нарисовать диаграмму распределения ip адресов по городам/регионам/странам.
   Список ip адресов находится в файле `ips.txt` по 1 ip адресу в строке

   Как это делать?
   1. Получить данные о местоположении по заданному ip, делая запросы к API https://ipinfo.io/products/ip-geolocation-api
      * Необходимо будет зарегистрироваться на сайте и получить свой токен, с помощью которого и делать запросы
   2. Вытащить из полученных данных информацию о _городе_, _регионе_ или _стране_. 
   3. Пользоваться библиотеками `requests`, `json`, `plotly`, `matplotlib`


### 5. Такое сложное задает 
* #### Universal

   В ДЗ4, возможно, Вам предлагалось заменить свой словарь (dict) на defaultdict из collections:
   https://docs.python.org/3/library/collections.html#defaultdict-objects.

   В этой домашке Вам предстоит самостоятельно написать этот класс

   1. Пример использования:
   ```python
      s = 'mississippi'
      d = mydefaultdict(int)
      for k in s:
            d[k] += 1
      sorted(d.items())
   # [('i', 4), ('m', 1), ('p', 2), ('s', 4)]
   ``` 
   2. Должен выполнять все действия, что и обычный dict. Но должен переопределить конструктор __init__, чтобы принять функцию, которая создает элементы, и при обращении оператором [] должен, при отсутствии элемента, создать его функцией, переданной в конструктор.

   3. Из примера: int() -> 0, те при изначальном обращении создастся 0 и к нему будет += 1

   4. Подсказка: правильная реализация не занимает более 15 строк