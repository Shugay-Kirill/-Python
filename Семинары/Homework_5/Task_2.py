# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def summ_number(first_number, second_number):
    if first_number == 0:
        return second_number
    return summ_number(first_number - 1, second_number + 1)

print(summ_number(8, 15))