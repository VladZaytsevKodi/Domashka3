#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в 
# обоих наборах.Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("ввести колиество элементов первого множества"))
m = int(input("ввести колиество элементов второго множества"))
listN = []
listM = []
for i in range(n):
    listN.append(int(input(f"введите - {i + 1} элемент первого множества")))
for i in range(m):
    listM.append(int(input(f"введите - {i + 1} элемент второго множества")))

print(f"первое множество - {listN}")
print(f"второе множество - {listM}")

setN = set(listN)
setM = set(listM)

print(setN.intersection(setM))

"""решение из подсказок не работает!
mol = [int(x) for x in input().split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in input().split()]
k = set(a)
for i in k:
set_1.add(i)
b = [int(x) for x in input().split()]
k1 = set(b)
for i in k1:
set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
print(i, end=' ')"""