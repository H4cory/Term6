# Зад.7 Функция - приема стринг и замества всички символи еднакви на първия с '*'
# def fix_start(s):
# fix_start('babble') # 'ba**le')
# fix_start('aardvark') # 'a*rdv*rk'
# fix_start('google') # 'goo*le'
# fix_start('donut') # 'donut'

def fix_start(s):
    result = ''
    for i in range (len(s)):
        if s[0] == s[i] and i != 0:
           result += '*'
        else:
            result += s[i]
    
    
    
    
    print(result)



fix_start('babble')
fix_start('aardvark')
fix_start('google')
fix_start('donut')