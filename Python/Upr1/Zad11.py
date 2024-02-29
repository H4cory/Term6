# Зад.11 Функция: разделя стринг на две половини.
# връща: a-front + b-front + a-back + b-back
# def front_back(a, b):
# front_back('abcd', 'xy') # 'abxcdy'
# front_back('abcde', 'xyz') # 'abcxydez'
# front_back('Kitten', 'Donut') # 'KitDontenut'

import math

def front_back(a, b):
    result = ''
    count_a = 0
    count_b = 0

    count_a = math.ceil(len(a)/2)
    count_b = math.ceil(len(b)/2)

    for i in range(count_a):
        result += a[i]
    for i in range(count_b):
        result += b[i]
    
    while count_a < len(a):
        result += a[count_a]
        count_a +=1

    while count_b < len(b):
        result += b[count_b]
        count_b +=1

    print(result)


front_back('abcd', 'xy') # 'abxcdy'
front_back('abcde', 'xyz') # 'abcxydez'
front_back('Kitten', 'Donut') # 'KitDontenut'