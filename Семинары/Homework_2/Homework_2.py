# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# *Пример:
# 4 4 -> 2 2
# 5 6 -> 2 *

from math import sqrt

summ = int(input("Введите сумму: "))
multiplication = int(input("Введите произведение: "))
if summ*summ < 4 * multiplication:
    print("Значений таких нет")
else:
    number_1 = (summ + sqrt(summ*summ - 4 * multiplication)) / 2
    number_2 = (summ - sqrt(summ*summ - 4 * multiplication)) / 2
    if number_1 == int(number_1) and number_2 == int(number_2):
        print(f"Первое число = {int(number_1)} \nВторое число = {int(number_2)}")
    else: 
        print("Значения не целые")
