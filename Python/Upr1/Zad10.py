# Зад.10 Функция: намира първото срещане на подстринга 'not' и 'bad'.
# Ако 'bad' е след 'not' замества целия израз 'not'...'bad' със стринга 'good'
# def not_bad(s):
# not_bad('This movie is not so bad') # 'This movie is good'
# not_bad('This dinner is not that bad!') # 'This dinner is good!'
# not_bad('This tea is not hot') # 'This tea is not hot'
# not_bad("It's bad yet not") # "It's bad yet not"
import sys

def not_bad(s):
    i = 0
    result = ''
    start_of_not = -1
    start_of_bad = -1

    while i < len(s) - 2:
        if (s[i] + s[i+1] + s[i+2]) == 'not':
            start_of_not = i
        elif (s[i] + s[i+1] + s[i+2]) == 'bad':
            start_of_bad = i
        i += 1
        
    i =0

    if start_of_not < start_of_bad and start_of_bad != -1 and start_of_not != -1:
        while i < len(s):
            if start_of_not == i:
                result += 'good'
                i = len(s)
            else:
                result += s[i]
                i += 1
    else:
        result = s

    print(result)
            

not_bad('This movie is not so bad') # 'This movie is good'
not_bad('This dinner is not that bad!') # 'This dinner is good!'
not_bad('This tea is not hot') # 'This tea is not hot'
not_bad("It's bad yet not") # "It's bad yet not"