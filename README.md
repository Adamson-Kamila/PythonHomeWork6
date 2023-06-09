### Task1
> Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.

Для решения этой задачи брались такие условия: 
* нормальная продолжительность рабочего времени - 40 часов в неделю (ст.91 ТК РФ), 
* производственный календарь, где указано плановое количество рабочих дней и часов, 
* фактически отработанное время,
* премия в %.

Формула для расчета заработной платы - оклад // на плановое количество рабочих часов в расчтеном месяце, умножается на фактически отработанное время + премия.
Премия считается оклад // 100 * премию.

Если работнику по каким-то причинам не начисляют премию, то программа возвращает результат 

> оклад // плановое рабочее время * фактическое

### Task2
> Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
Реализуйте вариант без и с LC

Задача решена с помощью двух функций. В первой функции генерируется список из рандомных значений, в заданном мною диапазоне и вторая функция выбирает значения, которые соответствуют моему заданному условию. Решение реализовано с помощью цикла for и LC.

### Task3
> Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и LC. 

Создала список с необходимыми параметрами. И методом деления без остатка выяснила сколько чисел из созданного списка кратны 20 и 21.
Решения представлены в две строки и в одну. Единтсвенный момент, в решении через одну строку я не смогла разделить полученный результат для 20 и 21.

### Task4
> Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать LC.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]

Генерируем рандомный список (генератор списков это просто must have). И через цикл проходимся по всему списку, проверяем каждое число. Если число одно и не имеет повторений, то добавляем его в новый список. 

### Task30

> Заполните массив элементами арифметической прогрессии. Её первый элемент,
разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.

Для решения этой задачи исползуем три переменные:

> первый элемент в списке

> разность между элементами

> длина списка

И опять же, через генератор заполняем список. Принцип генератора:

> list = [выражение с переменной  for переменная in итерабельный объект (из него будут браться переменные)]


### Task32

> Определить индексы элементов массива (списка), значения которых принадлежат
заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

Создаем две переменные - минимальный диапазон и максимальный.
Генерируем список с рандомными значениями и заданной нами длиною.
С помощью цикла проходимся по списку, выбираем необходимые нам числа, и формируем из них новый список.
Мною представлено три вида генератора списка.
1. Выводит только индексы значений, удовлетворяющих условию.
2. Выводит и индекс и значения.
3. Выводит и индекс и значения, в этом генераторе использовалась функция "enumerate".

### TaskStar1

> Дано 20+ значное целое число, проверить его на делимость на 7
Ввод 234523642345789812354678654323454919865
Вывод Делится

Если задачу понимать буквально, как она написана, то и задача удивляет, почему она попала в категорию задач со *.

> Какое условие, такое и решение.

> a = int(input('Введите 20 + значное число: '))
print('делится' if a % 7 == 0 else 'нет')

Но на самом деле для решения этой задачи надо использовать математический подход. а именно - признаки делимости на 7.
Их несколько, в этой задачи я продемонстрировала 1 из способов, по формуле
a // 10 * 3 + a % 10, где a - введенное пользователем число. Задача решена рекурсивным методом. Где условия выхода, кода а == 7, и проверка, если число, котрое мы приведем к типу str, то есть его длина == 1, значит введенное a не делится на 7. 