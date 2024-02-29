# Функция - приема списък от числа, премахва всички съседни повтарящи се елементи.
# def remove_adjacent(nums):
# remove_adjacent([1, 2, 2, 3]) # [1, 2, 3]
# remove_adjacent([2, 2, 3, 3, 3]) # [2, 3]

def remove_adjacent(userInput):
    i = 0
    while i < len(userInput) - 1:
        if userInput[i] == userInput[i+1]:
            del userInput[i]
        else:
            i +=1
    
    print(userInput)
   

remove_adjacent([1, 2, 2, 3])
remove_adjacent([2, 2, 3, 3, 3])