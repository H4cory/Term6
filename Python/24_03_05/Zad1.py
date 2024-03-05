# III.	Задачи:
# 1.	Напишете клас Rectangle с атрибути за дължина и ширина.
# 1.1.	Създайте метод Perimeter() за изчисляване на периметъра
#  на правоъгълника и метод Area() за изчисляване на площта на
#  правоъгълника.

# 1.2.	Създайте метод display(), който показва дължината, 
# ширината, периметъра и площта на обект, създаден с помощта
#  на инстанция върху клас правоъгълник.

class Rectangle:
    def __init__(self, lenght, height):
        self.lenght = lenght
        self.height = height
    
    def Perimeter(self):
        self.P = self.lenght * 2 + self.height * 2
    
    def Area(self):
        self.S = self.lenght * self.height

    def Display(self):
        print(f"Lenght: {self.lenght}")
        print(f"Height: {self.height}")
        print(f"P: {self.P}")
        print(f"S: {self.S}")

rect1 = Rectangle(3,4)
rect1.Perimeter()
rect1.Area()
rect1.Display()
