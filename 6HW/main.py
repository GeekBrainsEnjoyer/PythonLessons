# # Задача 30: Заполните массив элементами арифметической
# # прогрессии. Её первый элемент, разность и количество
# # элементов нужно ввести с клавиатуры. Формула для
# # получения n-го члена прогрессии: a
# # n = a1 + (n-1) * d.
# # Каждое число вводится с новой строки.
# # Ввод: 7 2 5
# # Вывод: 7 9 11 13 15


# def arithmeticProgresion(a1, d, n):
#     arrOfElements = []
#     for i in range(1, n + 1):
#         element = a1 + (i - 1) * d
#         arrOfElements.append(element)

#     return arrOfElements

# firstElement = int(input("Input the first element: "))
# diff = int(input("Input the difference: "))
# quantityElements = int(input("Input the quantity of elements: "))
# print(arithmeticProgresion(firstElement, diff, quantityElements))


# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

arr = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

def findIndexes(array, min, max):
    arrOfIndexes = []
    for i in range(len(array)):
        if array[i] >= min and array[i] <= max:
            arrOfIndexes.append(i)
    return arrOfIndexes

min = int(input("Input the min: "))
max = int(input("input the max: "))

print(findIndexes(arr, min, max))