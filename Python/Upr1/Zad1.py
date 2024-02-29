# Напишете функция, която приема списък от стрингове и намира
# броя на стринговете, които са с дължина >=2 и първия и последния символ съвпадат.
# def match_ends(words):
# match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']) # 3
# match_ends(['', 'x', 'xy', 'xyx', 'xx']) # 2
# match_ends(['aaa', 'be', 'abc', 'hello']) # 1


def match_ends(userInput):
    n = 0
    for word in userInput:
        if len(word) >= 2 and word[-1] == word[0]:
            n += 1

    print(n)



match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
match_ends(['', 'x', 'xy', 'xyx', 'xx'])
match_ends(['aaa', 'be', 'abc', 'hello'])
#