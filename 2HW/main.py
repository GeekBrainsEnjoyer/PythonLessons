# # # Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# # # решкой, а некоторые – гербом. Определите минимальное число
# # # монеток, которые нужно перевернуть, чтобы все монетки были
# # # повернуты вверх одной и той же стороной. Выведите минимальное
# # # количество монет, которые нужно перевернуть.
# # # 5 -> 1 0 1 1 0
# # # 2

# # coins = int(input('Input quantitu of a coins: '))
# # count1 = 0
# # count2 = 0
# # i = 0

# # while i < coins :
# #     value = int(input('Input side of the coin: '))
# #     if value == 0 :
# #         count1 += 1
# #         i += 1
# #     elif value == 1 :
# #         count2 +=1
# #         i += 1
# #     else :
# #         print('Incorrect value')

# # if count1 <= count2 :
# #     print(count1)
# # else :
# #     print(count2)

# # Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# # школьница. Петя помогает Кате по математике. Он задумывает два
# # натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# # этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# # произведение P. Помогите Кате отгадать задуманные Петей числа.
# # 4 4 -> 2 2
# # 5 6 -> 2 3

# sum = int(input('Input sum: '))
# multi = int(input('Input multi: '))
# x = 0
# y = 0

# for tempX in range(sum) :
#     for tempY in range(sum) :
#         if sum == tempX + tempY and multi == tempX * tempY :
#             x = tempY
#             y = tempX
            
# print(f"x = {x}\ny = {y}")

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

N = int(input('Input the number: '))
twoToPower = 0
k = 0
while twoToPower < N :
    if twoToPower != 0 :
        print(twoToPower)
    twoToPower = pow(2, k)
    k += 1

