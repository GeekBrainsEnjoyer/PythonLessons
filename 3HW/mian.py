# # Задача 16: Требуется вычислить, сколько раз встречается некоторое
# # число X в массиве A[1..N]. Пользователь в первой строке вводит
# # натуральное число N – количество элементов в массиве. В последующих
# # строках записаны N целых чисел Ai
# # . Последняя строка содержит число X
# # 5
# # 1 2 3 4 5
# # 3
# # -> 1

# A = [i + 1 for i in range(int(input("Input number N: ")))]
# X = int(input("Input number X: "))
# print(A)
# print(A.count(X))

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5


A = [1 + i for i in range(int(input("Input number N: ")))]
X = float(input("Input number X: "))
print(A)

closeValue = 0
for j in A:
    if A[j - 2] <= X and A[j - 1] > X:
        closeValue = A[j-2]
    elif X >= A[-1]:
        closeValue = A[-1]

print(closeValue)
