# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# empty = 'a a a b c a a d c d d'
# list_empty = empty.split()
# direction = {}
# res_str = ' '
# for i in list_empty:
#     if direction.get(i) != None:
#         direction[i] += 1
#         res_str += i+f'_{direction[i]} '
#     else:
#         direction[i] = 0
#         res_str += f'{i} '
# print(res_str)

# input_str = 'a a a b c a a d c d d'

# input_list_str = input_str.split()
# temp = {}
# res_str = ''
# for i in input_list_str:
#     if temp.get(i) != None:
#         temp[i] = temp.get(i) + 1
#         res_str += f'{i}_{temp[i]} '
#     else:
#         temp[i] = 0
#         res_str += f'{i} '
# print(temp)
# print(res_str)

# input_str = 'a a a b c a a d c d d'

# input_lst = input_str.split()
# print(input_lst)
# res = []

# for i in range(len(input_lst)):
#     x = input_lst[:i]
#     if x.count(input_lst[i]) == 0:
#         res.append(input_lst[i])
#     else:
#         res.append(f'{input_lst[i]}_{x.count(input_lst[i])}')
# print(res)
# out_str = ' '.join(res)
# print(out_str)


"""Задача №27. Решение в группах
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
Output: 13"""
# input_str = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# list_str = input_str.lower().split()
# print(list_str)
# res_str = set(list_str)
# print(res_str)
# print(len(res_str))

'''Задача №29. Решение в группах
Ваня и Петя поспорили, кто быстрее решит
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не
такими смышлеными. Никто из ребят не смог до
конца сделать это задание. Они решили так: у кого
будет меньше ошибок в коде, тот и выиграл спор. За
помощью товарищи обратились к Вам, студентам.
Примечание: Программные коды на следующих
слайдах'''

# Ваня:

n = int(input())
max_number = n
while n != 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(max_number)

# Петя:
n = int(input())
max_number = 0
while n != 0:
    n = int(input())
if max_number < n:
    max_number = n 
print(max_number)

