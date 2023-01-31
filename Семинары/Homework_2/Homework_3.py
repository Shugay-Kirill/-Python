# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

input_number = int(input("Введиие целое число: "))
count = 0
while 2**count <= input_number:
    print(2**count)
    count += 1
    