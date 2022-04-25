import sys
import time



# 1. Создание функции которая
# принимает N целых чисел и возвращает список квадратов эих чисел
def kvadrat (b):
    a = float(b ** 2)
    return a

def degree (b, c):
    b = float(b ** c)
    return b

a = float(input("Возвести в квадрат - нажмите 2, возвести в другую степень - "
          "нажмите 0: "))

if a != 0 and a != 2:
    print ('Вы не внимательны и ввели', a, 'вместо 0 или 2, пока')
    sys.exit()

b = float(input("Введите число, которое следует возвести в степень: "))

if a == 2:
    b = float(kvadrat(b))
    print(b)
    sys.exit()

if a == 0:
    c = float(input("Введите степень, в которую следует возвести: "))
    b = float(degree(b, c))
    print(b)

#функция, которая на вход принимает список из целых чисел, и возвращает только чётные/нечётные/простые числа


d = input("Введите список целых чисел, разделенных пробелом: ").split()
d = list(map(int, d))
e = float(input("Выбрать нечетные - нажмите 1, выбрать четные - "
          "нажмите 2, выбрать простые - нажмите 3: "))

def choice(d, e):

    if e < 1 or e > 8:
        print('Вы ввели число', e, ',а нужно 1, 2 или 3!')

    if e == 1:
        print([i for i in d if i % 2 != 0])

    if e == 2:
        print([i for i in d if i % 2 == 0])

    if e == 3:
        print([x for x in d
               if not [n for n in range(2, x) if not x % n]])





choice(d, e)




# декоратор для замера времени выполнения функции

def one ():
    t1 = time.perf_counter()
    print('Время начала операции: ', t1)

def two ():
    t2 = time.perf_counter()
    print('Время конца операции: ', t2)

#декоратор, который показывает вложенные входы в функцию


def trace(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper



@trace
def fibo(n):
    fib1 = 1
    fib2 = 1
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return fib2

fibo(120)
fibo(120)
fibo(120)

print(fibo.count)
