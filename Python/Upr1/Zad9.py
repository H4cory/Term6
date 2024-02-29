# Зад.9 Функция - приема стринг, ако е дължина поне 3 добавя 'ing' в края.
# Освен ако не завършва на 'ing' тогава добавя 'ly'.
# ако стринга е с дължина < 3 не го променя
# def verbing(s):
# verbing('hail') # 'hailing'
# verbing('swiming') # 'swimingly'
# verbing('do') # 'do'

def verbing(s):
    if len(s) >= 3:
        if (s[-3] + s[-2] + s[-1]) == 'ing':
            s+= 'ly'
        else:
            s+= 'ing' 
 
    print(s)

verbing('hail')
verbing('swiming')
verbing('do')