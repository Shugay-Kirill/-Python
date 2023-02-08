# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
from random import randint

first_list = []
second_list = []
length_first_list = int(input("Введите длинну пергово набора чисел: "))
length_second_list = int(input("Введите длинну второго набора чисел: "))

min_number_random = 0
max_number_random = 10

for item in range(length_first_list):
    first_list.append(randint(min_number_random, max_number_random))
for item in range(length_second_list):
    second_list.append(randint(min_number_random, max_number_random))

result_list = []
check_list = []
if length_first_list > length_second_list:
    check_list = second_list
else:
    check_list = first_list
    
for item in check_list:
    if first_list.count(item) != 0 and second_list.count(item) != 0 and result_list.count(item) == 0:
        for _ in range(min(first_list.count(item), second_list.count(item))):
            result_list.append(item)
            
# print(first_list)
# print(second_list)
print(result_list)

    
