# Задача 3:
# Напишите программу, которая на вход принимает 5 чисел
# и находит максимальное из них.
from random import randint
import os

# print(f'OS = {os.name}')
if os.name == 'nt':
    os.system('CLS')

# без random:
# nums = 5
# max_num = int(input('Введите число 1: '))
# for i in range(2, nums + 1):
#     num = int(input(f'Введите число {i}: '))
#     if num > max_num:
#         max_num = num
# print(f'max -> {max_num}')

# через list, map и split
a= list(map(int, input('Введите числа через пробел: ').split()))  # split разрезает строку чисел, введенных через пробел
print(max(a))

# с random:
# nums = 5
# rnd_min = 0
# rnd_max = 100
# nums_list = []
# for i in range(1, nums + 1):
#     if i == 1:
#         num = randint(rnd_min, rnd_max)
#         nums_list.append(num)
#         max_num = num
#     else:
#         num = randint(rnd_min, rnd_max)
#         nums_list.append(num)
#         if num > max_num:
#             max_num = num
# print(f'{nums_list} -> {max_num}')
