#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
#Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
#а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих
 #чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import math
s = int(input("Введите суму чисел"))
p = int(input("Введите произведение чисел"))
d = s**2 - 4*p
y = 0

if (d >= 0):
    y = (s + math.sqrt(d))/2
    x = s - y
    print("первое число", y, "второе число", x)
else:
    print("Данные не верные")
