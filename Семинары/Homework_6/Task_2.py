# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
number_list = []
legth_array = 5
max_number = 20
min_number = 10
index_list = []
for i in range(legth_array):
    number_list.append(randint(0,20))
    if number_list[i] < max_number and number_list[i] > min_number:
        index_list.append(i)
print(number_list)
print(index_list)
    