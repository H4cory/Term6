# Зад.3 Функция - приема списък от непразни кортежи и сортира списъка в нарастващ ред на
# последните елементи на всеки кортеж.
# def sort_last(tuples):
# sort_last([(1, 3), (3, 2), (2, 1)]) # [(2, 1), (3, 2), (1, 3)])
# sort_last([(2, 3), (1, 2), (3, 1)]) # [(3, 1), (1, 2), (2, 3)])
# sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]) # [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

def sort_last(user_input):
   user_input.sort(key=lambda kortej: kortej[-1])
   print(user_input)


sort_last([(1, 3), (3, 2), (2, 1)])
sort_last([(2, 3), (1, 2), (3, 1)])
sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])