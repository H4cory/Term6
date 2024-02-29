# Зад.12 Функция: приема списък от числа,
# връща списък само от четните числа.

def sort_even(userInput):
    result = [number for number in userInput if number % 2 == 0]
    print (result)

sort_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
sort_even([87, 46, 90, 123, 473, 324, 86])