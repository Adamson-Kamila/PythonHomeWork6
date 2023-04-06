# 1. Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений
# необходимо запускать скрипт с параметрами.

from sys import argv

salary = int(argv[1])
working_hours = int(argv[2])
worked_hours = int(argv[3])
prize = int(argv[4])


def get_wages(salary, working_hours, worked_hours, prize):
    if prize == 0:
        return salary // working_hours * worked_hours
    return salary // working_hours * worked_hours + salary * prize // 100

print(get_wages(salary, working_hours, worked_hours, prize))
