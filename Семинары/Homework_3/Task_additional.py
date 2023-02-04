# Доп задача
# 1. часть
# словарь с многочленами, где коэфф рандомно, степень по убыванию идет до 0 степени(полиминомиальная функция) и разбить по словопю, ключи степень
# 2. часть
# сложить 2 многочлена(полиномиальной функции)

# summ Kn*Xn**n

from random import randint

def creation_dictionary(input_power, x):
    dictionary = {}
    for i in range(input_power + 1):
        coefficient = randint(0,10)
        if (coefficient != 0):
            dictionary.update({i: [coefficient, pow(x, i)]})
    return dictionary
  
input_power = int(input("Введите значение степени: ")) 
x = int(input("Введите значение X: "))   
dictionary_1 = creation_dictionary(input_power, x)
dictionary_2 = creation_dictionary(input_power, x)
result_dictionary = {}

for i in range(input_power + 1):
    if i in dictionary_1 and i in dictionary_2:
        result_dictionary.update({i: [dictionary_1[i][0] + dictionary_2[i][0], dictionary_1[i][1]]})
    elif i in dictionary_1:
        result_dictionary.update({i: [dictionary_1[i][0], dictionary_1[i][1]]})
    elif i in dictionary_2:
        result_dictionary.update({i: [dictionary_2[i][0],dictionary_2[i][1]]})

print("dictionary_1 = ",dictionary_1)
print("dictionary_2 = ", dictionary_2)
print("result_dictionary = ",result_dictionary)






