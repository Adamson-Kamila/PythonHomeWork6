# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
#
# Реализуйте вариант без и с LC
import random

def get_list():
    list = [random.randint(0, 300) for i in range(10)]
    print(list)
    return list


list = get_list()


def get_new_list(list):
    list1 = [list[i + 1] for i in range(0, len(list) - 1) if list[i] < list[i + 1]]
    print(list1)


get_new_list(list)


def get_for(list):
    list1 = []
    for i in range(0, len(list)-1):
        if list[i] < list[i + 1]:
            list1.append(list[i+1])
    print(list1)


get_for(list)
