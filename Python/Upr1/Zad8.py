# Зад.8 Функция - приема два стринг и връща един стринг съдържащ двата разделени с
# интервал.
# разменя първите два символа на двата стринга.
# def mix_up(a, b):
# mix_up('mix', 'pod') # 'pox mid'
# mix_up('dog', 'dinner') # 'dig donner'
# mix_up('gnash', 'sport') # 'spash gnort'
# mix_up('pezzy', 'firm') # 'fizzy perm'


def mix_up(a, b):
    result = ''
    i = 0
    while i < len(a):
        if i == 0:
            result = result + b[0] + b[1]
            i += 2
        else:
            result+=a[i]
            i += 1

    result += ' '

    i = 0
    while i < len(b):
        if i==0:
            result = result + a[0] + a [1]
            i += 2
        else:
            result += b[i]
            i += 1


    print(result)


mix_up('mix', 'pod')
mix_up('dog', 'dinner')
mix_up('gnash', 'sport')
mix_up('pezzy', 'firm')