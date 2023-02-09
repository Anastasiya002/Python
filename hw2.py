''''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное 
количество монет, которые нужно перевернуть
5 -> 1 0 1 1 0
2
'''''
# count_1 = 0 
# count_0 = 0
# obverse = 0 
# reverse = 0 
# n = int(input()) 
# for _ in range(n): 
#     coin = int(input()) 
#     if coin > 0: 
#         obverse += 1 
#         count_1 = obverse    
#     elif coin <= 0:
#         reverse += 1
#         count_0 = reverse
# if reverse > obverse:
#     print(obverse)
# else:
#     print(reverse)

'''''
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
4 4 -> 2 2
5 6 -> 2 3
'''''
# x1 + x2 = summa = 4 = b
# x1 * x2 = proizvedeniye = 4 = c
# x^2 - 4x + 4 = 0
# summa = int(input()) 
# proizvedeniye = int(input())  
# a = 1
# D = summa**2 - 4*a*proizvedeniye
# if D < 0:
#     print('Корней нет')
# elif D == 0:
#     x = summa / (2 * a)
#     print(f'x = y = {x}')
# else:
#     x1 = (summa + D ** 0.5) / (2 * a)
#     x2 = (summa - D ** 0.5) / (2 * a)
#     print(f'x = {x1}')
#     print(f'y = {x2}')


# x = int(input())
# y = int(input())
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(i, j)


# guessNumbers(s = 5, p = 6)
'''''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
10 -> 1 2 4 8 
'''''
p = int(input()) 
N = int(input())
i = 0
while p ** i <= N:
   print(f'{N} -> {p ** i}')
   i += 1


# n = int(input("Введите число: "))
# m = 1
# while m < n:
#     print(m, end=' ')
#     m = m * 2
