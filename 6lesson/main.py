# # # # Задача №39. Решение в группах
# # # # Даны два массива чисел. Требуется вывести те элементы
# # # # первого массива (в том порядке, в каком они идут в первом
# # # # массиве), которых нет во втором массиве. Пользователь вводит
# # # # число N - количество элементов в первом массиве, затем N
# # # # чисел - элементы массива. Затем число M - количество
# # # # элементов во втором массиве. Затем элементы второго массива
# # # # Ввод: Вывод:
# # # # 7     3 3 2 12
# # # # 3 1 3 4 2 4 12
# # # # 6
# # # # 4 15 43 1 15 1

# # # N = int(input("Input N: "))
# # # arr1 = [int(input("Input element: ")) for i in range(0, N)]
# # # M = int(input("Input M: "))
# # # arr2 = [int(input("Input element: ")) for i in range(0, M)]

# # # diff = []

# # # for i in range(len(arr1)):
# # #     count = 0
# # #     for j in range(len(arr2)):
# # #         if arr1[i] == arr2[j]:
# # #             count += 1
# # #     if count == 0:
# # #         diff.append(arr1[i])

# # # print(arr1)
# # # print(arr2)
# # # print(diff)

# # # Задача №41. Решение в группах
# # # Дан массив, состоящий из целых чисел. Напишите
# # # программу, которая в данном массиве определит
# # # количество элементов, у которых два соседних и, при
# # # этом, оба соседних элемента меньше данного. Сначала
# # # вводится число N — количество элементов в массиве
# # # Далее записаны N чисел — элементы массива. Массив
# # # состоит из целых чисел.
# # # Ввод:       Ввод:
# # # 5           5
# # # 1 2 3 4 5   1 5 1 5 1
# # # Вывод:      Вывод:
# # # 0           2

# # N = int(input("Input N: "))
# # arr1 = [int(input("Input element: ")) for i in range(0, N)]
# # count = 0
# # for i in range(len(arr1) - 1):
# #     if arr1[i] > arr1[i + 1] and arr1[i] > arr1[i - 1]:
# #         count += 1

# # print(count)

# # Задача №43. Решение в группах
# # Дан список чисел. Посчитайте, сколько в нем пар
# # элементов, равных друг другу. Считается, что любые
# # два элемента, равные друг другу образуют одну пару,
# # которую необходимо посчитать. Вводится список
# # чисел. Все числа списка находятся на разных
# # строках.
# # Ввод:         Вывод:
# # 1 2 3 2 3     2

# arr = [1, 2, 3, 2, 5, 6, 4, 5, 3]
# count = 0
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[j] == arr[i]:
#             count += 1

# print(count)

# Задача №45. Общее обсуждение
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:         Вывод:
# 300           220 284
