# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# 2 * 2 * 2 * 2 * 2
# 5   4   3   2   1


def pow_number(first_number, second_number):
    if second_number == 1:
        return first_number
    return first_number * pow_number(first_number, second_number-1)

print(pow_number(2, 5))
