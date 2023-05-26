# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

coins = int(input('Input quantitu of a coins: '))
count1 = 0
count2 = 0
i = 0

while i < coins :
    value = int(input('Input side of the coin: '))
    if value == 0 :
        count1 += 1
        i += 1
    elif value == 1 :
        count2 +=1
        i += 1
    else :
        print('Incorrect value')

if count1 <= count2 :
    print(count1)
else :
    print(count2)