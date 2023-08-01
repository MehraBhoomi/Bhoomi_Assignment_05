# Challenge 01]  In this challenge, you need to implement a method that squares
#                passing variables and returns their sum.
# Problem statement: Implement a class Point that has three properties and a method.
#                    All these attributes (properties and methods) should be public. 
#                    This problem can be broken down into two tasks:
# Task 1: 👉 Implement a constructor to initialize the values of three properties: x, y, and z.
# Task 2: 👉 Implement a method, sqSum(), in the Point class which squares x, y, and z and returns their sum.
# Sample properties 1, 3, 5
# Sample method output 35
# Coding exercise Create a class Point with three properties: x, y, and z.

class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        sum = 0 
        l = [self.x, self.y, self.z]
        for i in l:
            sum = sum + i**2
        print(sum) 
        return ""
    
sample = Point(1,3,5)
sample.sqSum()       #35







# Challenge 02] Implement a Calculator Class
#               In this exercise, you have to implement a calculator that can perform addition, 
#               subtraction, multiplication, and division.
#               Problem statement Write a Python class called Calculator by completing the tasks below:
# Task 1
# 👉 Initializer
# Implement an initializer to initialize the values of num1 and num2. Properties
# • num1
# • num2
# Task 2
# 👉 Methods
# • add() is a method that returns the sum of num1 and num2.
# • subtract() is a method that returns the subtraction of num1 from num2.
# • multiply() is a method that returns the product of num1 and num2.
# • divide() is a method that returns the division of num2 by num1.
# Input - Pass numbers (integers or floats) in the initializer.
# Output - addition, subtraction, division, and multiplication

# Sample input
# obj = Calculator(10, 94)
# obj.add()
# obj.subtract()
# obj.multiply()
# obj.divide()

# Sample output
# 104
# 84
# 940
# 9.4



class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print(self.num1+ self.num2)
        return ""

    def subtract(self):
        print(self.num2-self.num1)
        return ""
    
    def multiply(self):
        print(self.num1*self.num2)
        return ""
    
    def divide(self):
        print(self.num2/self.num1)
        return ""
    
obj = Calculator(10, 94)
obj.add()            #104
obj.subtract()       #84
obj.multiply()       #940
obj.divide()         #9.4







# Challenge 03] Implement the Complete Student Class
#               In this challenge, you will implement a student class
#               Problem statement
# Implement the complete Student class by completing the tasks below
# Task
# 👉 Implement the following properties as private:
# • name
# • rollNumber
# 👉 Include the following methods to get and set the private properties above:
# • getName()
# • setName()
# • getRollNumber()
# • setRollNumber()
# 👉 Implement this class according to the rules of encapsulation.
# Input - Checking all the properties and methods
# Output - Expecting perfectly defined fields and getter/setters
# Note: Do not use initializers to initialize the properties. Use the set methods to do so.
# If the setter is not defined properly, the corresponding getter will
# also generate an error even if the getter is defined properly.

class Student:

    def setName(self, x):
        self._Name = x
    def getName(self):
        return self._Name
    def setRollNumber(self,y):
        self._Rollno = y
    def getRollNumber(self):
        return self._Rollno
    
a = Student()
a.setName("Ram")
print(a.getName())       #Ram
a.setRollNumber(16)
print(a.getRollNumber())      #16









# Challenge no. 04] Implement a Banking Account
#                   In this challenge, you will implement a banking account using the concepts of inheritance.
#                   Problem statement
# Implement the basic structure of a parent class, Account, and a child class, SavingsAccount.
# Task 1
# 👉 Implement properties as instance variables, and set them to None or 0.
# Account has the following properties:
#     • title
#     • Balance
# SavingsAccount has the following properties:
#     • interestRate
# Task 2
# Create an initializer for Account class. The order of parameters should be the following, 
# where Ashish is the title, and 5000 is the account balance:
# Account("Ashish", 5000)
# Task 3
# Implement properties as instance variables, and set them to None or 0.
# Create an initializer for the SavingsAccount class using the initializer of the Account class in the order below:
# Account("Ashish", 5000, 5)
# Here, Ashish is the title and 5000 is the balance and 5 is the interestRate.

class Account:

    def __init__(self, title = None, balance = 0):
        self.title = title
        self.balance = balance

        
class SavingsAccount(Account):

    def __init__(self,title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate


Account("Ashish", 5000)
SavingsAccount("Ashish", 5000, 5)









# Challenge no. 05] Handling a Bank Account
#                   In this challenge, you will define methods for handling a bank account using concepts of inheritance.
#                   Problem statement
#                   In this challenge, we will be extending the previous challenge and implementing methods in the parent class and its corresponding child class.
#                   The initializers for both classes have been defined for you.
#  Task 1
#    In the Account class, implement the getBalance() method that returns balance.
#  Task 2
#    In the Account class, implement the deposit(amount) method that adds amount to the balance.
#    It does not return anything.

# Sample input
# balance = 2000
# deposit(500)
# getbalance()
# Sample output
# 2500

#  Task 3
#    In the Account class, implement the withdrawal(amount) method that subtracts the amount from the balance.
#    It does not return anything.

# Sample input
# balance = 2000
# withdrawal(500)
# getbalance()
# Sample output
# 1500

#  Task 4
#    In the SavingsAccount class, implement an interestAmount() method that returns the interest amount of the current balance.
#    Below is the formula for calculating the interest amount:
#    interestAmount = (interestRate*balance)/100
# Sample input
# balance = 2000
# interestRate = 5
# interestAmount()
# Sample output
# 100
# Note: A new SavingsClass object is initialized at the end of the code and test results will be based on it.
# # #code to test - do not edit this

# # demo1 = SavingsAccount("Ashish", 2000, 5)   # initializing a SavingsAccount object

class Account:
    Bank = "State Bank of India"

    def __init__(self, title=None, balance=0):
        self._title = title
        self._balance = balance

    def deposit(self,amount):
        self._balance = self._balance + amount

    def withdrawal(self, amount):
        self._balance = self._balance - amount

    def getBalance(self):
        return self._balance
        
class SavingsAccount(Account):

    def __init__(self,title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.interestRate*self._balance)/100

# Task 1 & 2]
x = Account("Ashish", 2000)
x.deposit(500)
print(x.getBalance())         #2500

# Task 3]
y = Account("Bhoomi", 2000)
y.withdrawal(500)
print(y.getBalance())          #1500

# Task 4]
z = SavingsAccount("Ravi", 2000, 5)
print(int(z.interestAmount()))    #100


# TEST CODE
demo1 = SavingsAccount("Ashish", 2000, 5)   # initializing a SavingsAccount object

demo1.deposit(500)
print(demo1.getBalance())  # Output: 2500

demo1.withdrawal(500)
print(demo1.getBalance())  # Output: 2000

print(demo1.interestAmount())  # Output: 100
