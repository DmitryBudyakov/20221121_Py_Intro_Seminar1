# Задача 5:
# Напишите программу, которая будет принимать на вход дробь
# и показывать первую цифру дробной части числа.
# Примеры:
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

a = float(input('Введите число: '))
a_int = int(a * 10)
result = a_int % 10
print(f'{a} -> {result}')