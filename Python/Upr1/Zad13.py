# Зад.13 Функция: приема два списъка,
#  връща списък с общите елементи на двата списъка.

def unite_lists(userInput1, userInput2):
    set1 = set(userInput1)
    set2 = set(userInput2)

    result = set1 & set2
    print(result)

unite_lists(['a', 'b', 3, 4, 8, 7, 'xy'], [0, 98, 'a', 3, 8, 'xy', 'j'])