# Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

list = [random.randint(0, 20) for i in range(10)]
print(list)
band_min = int(input('Введите минимальный диапазон: '))
band_max = int(input('Введите максимальный диапазон: '))

# выводит только индексы
# list1 = [i for i in range(0, len(list)) if band_min < list[i] < band_max]
# print(list1)

# выводит индексы и значения
# print([list.index(i) for i in list if band_min < i < band_max])

# функция enumerate выводит и индексы и значения.
list1 = [(idx, el) for idx, el in enumerate(list) if band_min < list[idx] < band_max]
print(list1)
