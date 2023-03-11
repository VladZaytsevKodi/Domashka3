#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
#  чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n =  int(input())
count_orel = 0
count_reska = 0
for i in range(n):
    x = int(input())
    if x == 0:
        count_orel += 1
    else:
        count_reska += 1
if count_reska > count_orel:
    print(count_orel)
else:
    print(count_reska)
    

