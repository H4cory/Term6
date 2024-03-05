# 2.	Създайте клас BankAccount, който представлява банкова
#  сметка, имаща като атрибути: accountNumber, 
# name (име на собственика на акаунта като низов тип), баланс.

# 2.1.	Създайте конструктор с параметри
# 2.2.	Създайте метод deposit(), който управлява действията за
#  депозит.

# 2.3.	Създайте метод withdrawal(), който управлява действията
#  за теглене.

# 2.4.	Създайте метод bankFees(), за да приложите банковите
#  такси с процент от 5% от балансовата сметка.

# 2.5.	Създайте метод display() за показване на подробности 
# за акаунта.

class BankAccount:
    def __init__ (self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    
    def deposit(self, sum):
        self.balance += sum
        self.bankFees(sum)

    def withdrawal(self, sum):
        self.balance -= sum
        self.bankFees(sum)

    def bankFees(self, sum):
        self.balance -= sum * 0.05

    def display(self):
        print(f"Account number: {self.accountNumber}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")
        print(" ")


Pesho = BankAccount("001", "Petyr", 0)
Pesho.display()
Pesho.deposit(100)
Pesho.display()
Pesho.withdrawal(50)
Pesho.display()
