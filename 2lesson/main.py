# # # Задача №13. Решение в группах
# # # Пользователь вводит число N – общее количество
# # # рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# # # располагается N целых чисел.
# # # Каждое число – среднесуточная температура в
# # # соответствующий день. Температуры – целые числа и лежат в
# # # диапазоне от –50 до 50
# # # Input: 6 -> -20 30 -40 50 10 -10
# # # Output: 2

# # count = 0
# # max = 0

# # n = int(input('Input a quantity of day: '))

# # for dayCount in range(n) :
# #     temperatureDay = int(input('Input a temperature of a day: '))
# #     if temperatureDay > 0 :
# #         count += 1
# #     elif count >= max :
# #         max = count
# #         count = 0

# #     if count > max :
# #         max = count

# # print('Max quantity of warm days is ', max)

# # Задача №9. Решение в группах
# # По данному целому неотрицательному n вычислите
# # значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# # чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# # while
# # Input: 5
# # Output: 120

# # N = int(input('Input number: '))
# # factorial = 1
# # count = 1

# # while count <= N :
# #     factorial *= count
# #     count += 1

# # if N == 0 :
# #     factorial = 1

# # print(factorial)

# # Задача №11. Решение в группах
# # Дано натуральное число A > 1. Определите, каким по
# # счету числом Фибоначчи оно является, то есть
# # выведите такое число n, что φ(n)=A. Если А не
# # является числом Фибоначчи, выведите число -1.
# # Input: 5
# # Output: 6

# A = int(input('Input number: '))
# fibonacci1 = 0
# fibonacci2 = 1
# temporary = 0
# count = 2

# if A > 1:
#     while fibonacci2 != A :
#         temporary = fibonacci1
#         fibonacci1 = fibonacci2
#         fibonacci2 += temporary
#         count += 1
#         if count < 9999 :
#             count = -1
#             break
#     print(count)

# else:
#     print('Incorrect input')

# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

N = int(input('Input qauntity of a watermelon: '))
biggestWatermelon = 0
smallestWatermelon = 100
count = 0

while count < N :
    watermalonMass = int(input(f"Input mass of watermelon: "))
    if watermalonMass > biggestWatermelon :
        biggestWatermelon = watermalonMass
    elif watermalonMass < smallestWatermelon :
        smallestWatermelon = watermalonMass
    count += 1

print(f'For me: {biggestWatermelon}, for the mother of my wife: {smallestWatermelon}')

