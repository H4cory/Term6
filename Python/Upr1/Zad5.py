# Зад.5 Функция - слива два сортирани списъка
# def linear_merge(list1, list2):
# linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']) # ['aa', 'bb', 'cc', 'xx', 'zz']
# linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']) # ['aa', 'bb', 'cc', 'xx', 'zz']
# linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']) # ['aa', 'aa', 'aa', 'bb', 'bb']

def linear_merge(list1, list2):
    result = list1 + list2
    result.sort()
    print(result)




linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])