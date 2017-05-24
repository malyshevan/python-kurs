# Задача 1
#x = input()
#def palindrom (x):
#    if x == x [::-1]:
#    	print ('True')
#    else: 
#        print ('False')
#palindrom (x)

# Задача 2

a = int(input('Координата х: '))
b = int(input('Координата у: '))
def funkcia(a, b):
	if a > 0 and b > 0:
		print ('Первая четверть')
	elif a < 0 and b > 0:
		print ('Вторая четверть')
	elif a < 0 and b < 0:
		print ('Третья четверть')
	elif a > 0 and b < 0:
		print ('Четвертая четверть')
	else:
	    print ('Точка находится на оси, она не относится ни к одной из четырех четвертей') 
funkcia(a, b)



