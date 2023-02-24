#Задача 2: Найдите сумму цифр трехзначного числа.
#*Пример:*
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) 

num =  int(input("Введите трехнаное число:"))
sum_digits = 0
while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10
print("Сумма цифр числа:", sum_digits)

