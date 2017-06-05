# Задача сотки

#a = 10 * 100
#b = 15 * 25
#c = int(a / b)
#print (c)
#d = a - b * 2
#print (d)


#Задача треугольник

#x1 = int(input('Введите точку x1: '))
#y1 = int(input('Введите точку y1: '))
#x2 = int(input('Введите точку x2: '))
#y2 = int(input('Введите точку y2: '))
#x3 = int(input('Введите точку x3: '))
#y3 = int(input('Введите точку y3: '))

#dlina_1 = (x1 - x2) ** 2 + (y1 - y2) ** 2
#dlina_2 = (x2 - x3) ** 2 + (y2 - y3) ** 2
#dlina_3 = (x3 - x1) ** 2 + (y3 - y1) ** 2

#if dlina_1 + dlina_2 == dlina_3:
#	print('Треугольник прямоугольный') 
#elif dlina_2 + dlina_3 == dlina_1:
#	print('Треугольник прямоугольный') 
#elif dlina_3 + dlina_1 == dlina_2:
#	print('Треугольник прямоугольный') 
#else:
#    print('Треугольник не прямоугольный')


#Задача тарелки

#plates = int(input('Количество тарелок: '))
#detergent = int(input('Количество моющего средства: '))
#detergent1 = detergent * 2
#detergent2 = - (plates - detergent1) / 2 
#plates1 = plates - detergent1  
#while 1:
#	if plates > detergent1:	
#		print ('Количество немытых тарелок:', plates1)   
#		break
#	if plates < detergent1:
#		print ('Количество оставшегося моющего средства:', detergent2) 
#		break 
#	else: 
#	    print ('Моющего средства как раз хватило')
#	    break


#Задача палиндром

#x = input()
#def palindrom (x):
#    if x == x [::-1]:
#    	print ('True')
#    else: 
#        print ('False')
#palindrom (x)


#Задача пузырек

x = [2, 3, 6, 5, 1] # массив с данными
def puzyrek(x):         #создаем функцию
    i = 1           #создаем счетчик           
    while i < len(x):   # создаем цикл 
        for j in range(len(x)-i):   #проверяем условие
            if x[j] > x[j + 1]: # если следующий элемент меньше предыдущего, тогда
                x[j], x[j+1] = x [j+1], x[j] # расставляем элементы списка в другом порядке
        i += 1 #увеличиваем счётчик
    return x
print(puzyrek(x)) #выводим результат
