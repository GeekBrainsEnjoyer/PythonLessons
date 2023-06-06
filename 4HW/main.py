# # Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# # Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# n = int(input("Input number n: "))

# nList = []
# mList = []

# for num in range(n):
#     nElement = int(
#         input(f"Input the value of element number {num + 1} in first list: "))
#     nList.append(nElement)

# m = int(input("Input number m: "))
# for num in range(m):
#     mElement = int(
#         input(f"Input the value of element number {num + 1} in second list: "))
#     mList.append(mElement)

# nList.sort()
# mList.sort()
# nList = set(nList)
# mList = set(mList)

# print(nList.intersection(mList))

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random
N = int(input("Input the number of plant: "))
countBluebarriesList = [random.randint(0, 10) for i in range(N)]

maxBarriesList = []
i = 2
for i in range(len(countBluebarriesList)):
    maxBarries = countBluebarriesList[i] + countBluebarriesList[i - 1] + countBluebarriesList[i - 2]
    maxBarriesList.append(maxBarries)

print(f"Quantity barries on one plant:\n{countBluebarriesList}")
print(f"Quntity barries on three plants:\n{maxBarriesList}")
print(f"Maximum barries: {max(maxBarriesList)}")

