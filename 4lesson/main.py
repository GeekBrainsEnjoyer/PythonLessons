# # Задача №25. Решение в группах
# # Напишите программу, которая принимает на вход
# # строку, и отслеживает, сколько раз каждый символ
# # уже встречался. Количество повторов добавляется к
# # символам с помощью постфикса формата _n.
# # Input: a a a b c a a d c d d
# # Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# # Для решения данной задачи используйте функцию
# # .split()

# text = "a a a b c a a d c d d"
# myList = text.split()
# dictionary = {}
# count = str()

# for letter in myList:
#     if letter in dictionary.keys():
#         dictionary[letter] += 1
#         count +=f"{letter}_{dictionary[letter]} "
#     else:
#         dictionary[letter] = 0
#         count += f"{letter} "

# print(count)
# print(dictionary)

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13


text = "She sells sea shells on the sea shore The shells \
that she sells are sea shells I'm sure. So if she sells sea \
shells on the sea shore I'm sure that the shells are sea \
shore shells"

text = text.replace("."," ").lower()
words = text.split()
uniqueWord = set(words)
print(uniqueWord)
print(len(uniqueWord))