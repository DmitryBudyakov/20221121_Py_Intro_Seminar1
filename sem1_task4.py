# Задача 4:
# Напишите программу, которая будет на вход принимать число N
# и выводить числа от -N до N

# без списка
N = int(input('Введите число: '))
print(f'{N} ->', end=' ')

for i in range(-N, N+1):
    if i == N:
        print(i)
    else:
        print(i, end=' ')

# со списком:
num = int(input('Введите число: '))
nums = []
for i in range(-num, num + 1):
    nums.append(i)
    
print(f'{num} ->', end=' ')
print(*nums)    # * распаковывает список, убирает []
