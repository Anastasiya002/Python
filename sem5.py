# def fib(n): 
#     if n in [1, 2]: 
#         return 1 
#     return fib(n - 1) + fib(n - 2) 

# list_1 = [] 
# for i in range(1, 10): 
#     list_1.append(fib(i - 2)) 
# print(list_1) # [1, 1, 2, 3, 5, 8, 13, 21, 34]

'''Задача №39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит 
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
Ввод: Вывод:
7 
3 1 3 4 2 4 12
6
4 15 43 1 15 1 
(каждое число вводится с новой строки)'''
# Решение 1
# def numbers(x):
#     list_1 = []
#     for _ in range(x):
#         list_1.append(int(input('Введите элемент массива: ')))
#     return list_1


# def diff_list(list_1, list_2):
#     list_3 = []
#     for i in list_1:
#         if i not in list_2:
#             list_3.append(i)
#     return list_3              
    

# n = int(input('Введите количество элементов первого массива: '))
# list_n = numbers(n)
# print(list_n)
# m = int(input('Введите количество элементов второго массива: '))
# list_m = numbers(m)
# print(list_m)

# print(diff_list(list_n, list_m))

# def lst_diff2(list_1: list, list_2: list):
# return [i for i in list_1 if i not in list_2] функция через list comre..блаблабла


# Решение 2
# import random
# import time
# first_list = [random.randint(1, 100) for _ in range(10 ** 6)]
# second_list = [random.randint(1, 100) for _ in range(10 ** 6)]

# start = time.perf_counter()
# for el in first_list:
#     if el not in second_list:
#         print(el)
# end = time.perf_counter()
# print(end - start)

# start = time.perf_counter()
# second_set = set(second_list)
# for el in first_list:
#     if el not in second_set:
#         print(el)
# end = time.perf_counter()
# print(end - start)

'''Задача №41. Решение в группах
Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве 
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.
Ввод: Ввод:
5 5
1 2 3 4 5 1 5 1 5 1
Вывод: Вывод:
0 2
(каждое число вводится с новой строки)'''

def numbers(x):  # функция для создания массива
    list_1 = []
    for _ in range(x):
        list_1.append(int(input('Введите элемент массива: ')))
    return list_1

def search_list(list_1): # функция для поиска числа 
    count = 0
    for i in range(1, len(list_1) - 1): # в диапазоне нашего листа от одного до длина списка -1. 
        if list_1[i - 1] < list_1[i] > list_1[i + 1]:
            count += 1
    return count

n = int(input('Введите количество элементов первого массива: '))
list_n = numbers(n) # вызов функции, которая создает массив
print(search_list(list_n)) # вызов функции поиска числа


'''Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод: Вывод:
1 2 3 2 3 2'''
# Вариант решения
# some_list = []
# while True:
#     number = int(input())
#     if number == 0:
#         break
#     some_list.append(number)

# count_dict = {}  # 2: 2, 3: 3, 4: 1, 5: 1

# for el in some_list:
#     if count_dict.get(el):
#         count_dict[el] += 1
#     else:
#         count_dict[el] = 1
        
# count = 0
# for value in count_dict.values():
#     count += value // 2
# print(count)


'''Задача №45. Решение в группах
Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 105
. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает).
Ввод: Вывод:
300 220 284'''

# def sum_div(n):
#     summa = 0
#     for i in range(1, n // 2 + 1):
#         if n % i == 0:
#             summa += i
#     return summa


# summ_dict = {}  # 284: 220,

# k = int(input())
# for number in range(2, k + 1):
#     if number in summ_dict:
#         if sum_div(number) == summ_dict[number]:
#             print(number, summ_dict[number])
#     summ_dict[sum_div(number)] = number

# Вариант 2   
def sum_divisors(num):
summ = 0
for i in range(1, num // 2 + 1):
if num % i == 0:
# print(f'{i = }')
summ += i
return summ


def friends_num(number):
for i in range(1, number):
j = sum_divisors(i)
if i < j <= number and i == sum_divisors(j):
print(i, j)

