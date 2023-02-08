# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
# Пример:
# 4 -> 1 2 3 4
# 9

from random import randint
length_bed = int(input("Введите длину грядки: "))
list_bed = []
min_number = 0
max_number = 10
for i in range(length_bed):
    list_bed.append(randint(min_number, max_number))

# way 1 

# max_harvest_0 = list_bed[len(list_bed) - 1] + list_bed[0] + list_bed[1]
# check_max = max_harvest_0 - list_bed[len(list_bed) - 1] + list_bed[2]
# max_harvest = 0
# max_harvest_len = list_bed[len(list_bed) - 1] + list_bed[len(list_bed) - 2] + list_bed[0]
# for i in range(1, len(list_bed) - 2):
#     check_max = check_max - list_bed[i - 1] + list_bed[i + 2]
#     if check_max > max_harvest:  
#         max_harvest = check_max
# print(list_bed)
# print(f"Максималный урожай = {max(max_harvest, max_harvest_0, max_harvest_len , check_max)}")


# way 2   

# max_harvest = 0
# for i in range(length_bed):
#     if i == 0:
#         if max_harvest < (list_bed[len(list_bed) - 1] + list_bed[i] + list_bed[i + 1]):
#             max_harvest = list_bed[len(list_bed) - 1] + list_bed[i] + list_bed[i + 1]
#     elif i == len(list_bed) - 1:
#         if max_harvest < list_bed[i - 1] + list_bed[i] + list_bed[0]:
#             max_harvest = list_bed[i - 1] + list_bed[i] + list_bed[0]
#     else:
#         if max_harvest < (list_bed[i - 1] + list_bed[i] + list_bed[i + 1]):
#             max_harvest = list_bed[i - 1] + list_bed[i] + list_bed[i + 1]
# print(f"Максималый урожай = {max_harvest}")
# print(list_bed)
