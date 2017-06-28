# Задача 1
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        b = a + b
        a = b - a
        yield a

for n in fibonacci(10):
    print(n)



# Задача 2
#import random
#from string import ascii_uppercase

#def ran(n):
#    yield ''.join([ascii_uppercase[random.randrange(len(ascii_uppercase))] for i in range(n)])

#gen = ran(int(input('Введите длину пароля: ')))
#print('пароль: {}'.format(next(gen)))


#Задача3
import random
import time
from time import sleep
from string import ascii_uppercase


def decorator(pausa):
    for x in range(1):
        time.sleep(3)
        print("Ваша операция выполняется...")
    return decorator

@decorator

def ran(n):
    yield ''.join([ascii_uppercase[random.randrange(len(ascii_uppercase))] for i in range(n)])

gen = ran(int(input('Укажите длину пароля: ')))
print('Пароль: {} '.format(next(gen)))



