# Задача 1
# m = int(750)
# n = int(700)
# print((n + m - 1) // n)

# # Задача 2
# a = int(input('Колличество учеников в классе "а": '))
# b = int(input('Колличество учеников в классе "b": '))
# c = int(input('Колличество учеников в классе "c": '))

# tablsA = (a + 1) // 2
# tablsB = (b + 1) // 2
# tablsC = (c + 1) // 2

# print(f'Для класса "a" необходимо {tablsA} парт')
# print(f'Для класса "a" необходимо {tablsB} парт')
# print(f'Для класса "a" необходимо {tablsC} парт')

# Задача 3
# intoTheWagon = int(input(
#     'В какой вагон по счету от головы сел Витя: '))
# wagonNumber = int(input('Какой номер имеет вагон: '))

# if (intoTheWagon == wagonNumber):
#     print('Без дополнительных данны это сделать не возможно')
# else:
#     print(intoTheWagon + wagonNumber - 1)

# Задача 4
yearNumber = int(input('Enter year namber: '))

if yearNumber % 4 == 0 and yearNumber % 100 != 0 or yearNumber % 400 == 0:
    print('YES')
else:
    print('NO')
