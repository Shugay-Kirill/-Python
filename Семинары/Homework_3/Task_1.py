# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

from random import randint 
list = []
random_max_number = 10
random_min_number = -10
long_list = int(input("Введите длинну списка: "))
for _ in range(long_list):
    list.append(randint(random_min_number,random_max_number))
    
search_number = int(input("Введите искомое число : "))  
near_max_number = random_max_number
near_min_number = random_min_number
count = 0
for i in range(long_list):
    if search_number > list[i] and list[i] > near_min_number:
        near_min_number = list[i]
    elif search_number < list[i] and list[i] < near_max_number:
        near_max_number = list[i]
    elif search_number == list[i]:
        count += 1
        
print(list)
if count != 0:
    print(f"Число {search_number} встречается в списке {count} раз")
else:
    if near_max_number - search_number == search_number - near_min_number:
        print(f"Числа одинаково блики к искомому числу {search_number} большее число = {near_max_number}, меньшее число = {near_min_number}")
    elif near_max_number != random_max_number and near_min_number == random_min_number:
        print(f"Бличайшее число к {search_number} = {near_max_number}")
    elif near_max_number == random_max_number and near_min_number != random_min_number:
        print(f"Бличайшее число к {search_number} = {near_min_number}")
    elif near_max_number - search_number > search_number - near_min_number:
        print(f"Бличайшее число к {search_number} = {near_min_number}")
    elif near_max_number - search_number < search_number - near_min_number:
        print(f"Бличайшее число к {search_number} = {near_max_number}")

