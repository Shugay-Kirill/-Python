# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-да

# Вывод: Парам пам-пам

input_strint = "пара-ра-рам рам-пам-папам па-ра-па-да".lower()
# input_strint = str.lower((input("Введите фразу Винни-Пуха: ")))

list_count_vowels = []
vowels = 0

for index in input_strint:
    if index == " ":
        list_count_vowels.append(vowels)
        vowels = 0
    elif index in ["а","о","и","у","е","ё","ю","я","ы","э"]:
        vowels +=1
list_count_vowels.append(vowels)

if list_count_vowels.count(list_count_vowels[0]) == len(list_count_vowels):
    print("Парам пам-пам")
else:
    print("Пам парам") 


