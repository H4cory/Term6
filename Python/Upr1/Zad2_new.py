# Зад.2 Напишете функция, която приема списък от стрингове и го връща сортиран,
# като всички стрингове започващи с 'x' са в началото.
# def front_x(words):
# front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']) # ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
# front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']) # ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
# front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']) # ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

def front_x(userInput):
   userInput.sort(key = lambda words: (words[0] != 'x', words))
   print(userInput)



front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
#