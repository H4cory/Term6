# Зад.2 Напишете функция, която приема списък от стрингове и го връща сортиран,
# като всички стрингове започващи с 'x' са в началото.
# def front_x(words):
# front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']) # ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
# front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']) # ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
# front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']) # ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

def front_x(userInput):
    counter = 0
    temp: str
    current_word = 0
    for word in userInput:
        if word[0] == 'x':
            userInput[current_word], userInput[counter] = userInput[counter], userInput[current_word]
            counter +=1
        current_word += 1

    print(userInput)



front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
#