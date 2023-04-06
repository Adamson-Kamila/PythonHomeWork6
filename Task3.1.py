# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и LC.

def get_list():
    list = [i for i in range(20, 241)]
    print(list)
    return list


list = get_list()


def multiples_numbers(list):
    # print(len([i for i in list if i % 20 == 0 or i % 21 == 0]))


    total1 = [i for i in list if i % 20 == 0]
    print(len(total1))
    total2 = [i for i in list if i % 21 == 0]
    print(len(total2))


multiples_numbers(list)
