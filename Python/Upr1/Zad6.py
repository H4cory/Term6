# Зад.6 Функция - приема стринг и връща стринг съдържащ първите два и последните два
# символа на първоначалния стринг.
# def both_ends(s):
# both_ends('spring') # 'spng'
# both_ends('Hello') # 'Helo'
# both_ends('a') # ''
# both_ends('xyz') # 'xyyz'

def both_ends(s):
    if len(s) >= 4:
        result = s[0] + s[1] + s[-2] + s[-1]
    elif len(s) <= 1:
        result = ''
    elif len(s) == 2:
        result = s[0] + s[0] + s[-1] + s[-1]
    elif len(s) == 3:
        result = s[0] +s[1] + s[1] + s[-1]
    print(result)


both_ends('spring')
both_ends('Hello')
both_ends('a')
both_ends('xyz')