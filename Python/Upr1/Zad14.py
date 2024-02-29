# Зад.14 Функция: приема число,
#  и намира всички негови делители.

def find_all_devisible_nums(user_input):
    i = 1
    while i <= user_input:
        if user_input % i == 0:
            print(i)
        i+= 1

find_all_devisible_nums(32)
print(" ")
find_all_devisible_nums(165)
print(" ")
find_all_devisible_nums(65)