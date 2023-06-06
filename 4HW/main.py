# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Input number n: "))

nList = []
mList = []

for num in range(n):
    nElement = int(
        input(f"Input the value of element number {num + 1} in first list: "))
    nList.append(nElement)

m = int(input("Input number m: "))
for num in range(m):
    mElement = int(
        input(f"Input the value of element number {num + 1} in second list: "))
    mList.append(mElement)

nList.sort()
mList.sort()
nList = set(nList)
mList = set(mList)

print(nList.intersection(mList))
