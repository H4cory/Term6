# Зад.15 Функция: приема число,
#  намира всички по-малки прости числа.

def find_prime(userInput):
    numbers = []
    i = 0
    j = 0
    while i < userInput:
        numbers.append(True)
        i += 1
    
    numbers[0] = numbers[1] = False
    i = 2

    while i * i < userInput:
        if numbers[i]:
            j = i * i
            while j < userInput:
                numbers[j] = False
                j += i
        i += 1

    i = 0

    while i < userInput:
        if numbers[i]:
            print(i)
        i +=1



find_prime(100) #2 	3 	5 	7 	11 	13 	17 	19 	23 	29 	31 	37 	41 	43 	47 	53 	59 	61 	67 	71	73 	79 	83 	89 	97

