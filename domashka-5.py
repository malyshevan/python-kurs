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

#for i in ran(10):
#    print(i)




