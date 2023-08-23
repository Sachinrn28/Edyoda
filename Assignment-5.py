#!/usr/bin/env python
# coding: utf-8

# # Challenge 1: Square Numbers and Return Their Sum

# Problem statement: Implement a class Point that has three properties and a method. All these attributes (properties and methods) should be public. This problem can be broken down into two tasks:
# 
# Task 1: 👉 Implement a constructor to initialize the values of three properties: x, y, and z.
# 
# Task 2: 👉 Implement a method, sqSum(), in the Point class which squares x, y, and z and returns their sum.
# 
# Sample properties 1, 3, 5
# 
# Sample method output 35

# In[37]:


class point:
    '''This is a class created get sum of the squar of three number'''
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def sq_sum(self):
        sqsumtot=(self.x**2+self.y**2+self.z**2)
        return f'The sum of the squar is:{sqsumtot}'


# In[38]:


a=point(1,3,5)
a.sq_sum()


# # Challenge 2: Implement a Calculator Class

# 🔴 In this exercise, you have to implement a calculator that can perform addition, subtraction, multiplication, and division.
# 
# Problem statement Write a Python class called Calculator by completing the tasks below:
# 
# Task 1
# 
# 👉 Initializer
# 
# Implement an initializer to initialize the values of num1 and num2. Properties
# 
# Task 2
# 
# 👉 Methods
# 
# • add() is a method that returns the sum of num1 and num2.
# • subtract() is a method that returns the subtraction of num1 from num2.
# • multiply() is a method that returns the product of num1 and num2.
# • divide() is a method that returns the division of num2 by num1.

# In[49]:


class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return f'The sum of the two numbers:{self.num1+self.num2}'
    def subtract(self):
        return f'The sum of the two numbers:{self.num2-self.num1}'
    def multiply(self):
        return f'The sum of the two numbers:{self.num1*self.num2}'
    def divide(self):
        return f'The sum of the two numbers:{self.num2/self.num1}'


# In[50]:


object2=calculator(10,94)
print(object2.add())
print(object2.subtract())
print(object2.multiply())
print(object2.divide())


# # Challenge 3: Implement the Complete Student Class

# Implement the complete Student class by completing the tasks below
# 
# Task
# 
# 👉 Implement the following properties as private:
# 👉 Include the following methods to get and set the private properties above:
# 
# • getName()
# • setName()
# • getRollNumber()
# • setRollNumber()

# In[69]:


class student:
    def __init__(self):
        self.name=None
        self.rollnumber=None
    def setName(self,newname):
        self.name=newname
    def getName(self):
        return self.name
    def setRollNumber(self,newnumber):
        if newnumber>0:
            self.rollnumber=newnumber
        else:
            return 'Enter valid rollnumber'
    def getRollNumber(self):
        return self.rollnumber


# In[77]:


obj=student()
obj.setName('Edyoda')
print(obj.getName())
obj.setRollNumber(240623)
print(obj.getRollNumber())


# # Challenge 4: Implement a Banking Account
# 🔴 In this challenge, you will implement a banking account using the concepts of inheritance.
# implement the basic structure of a parent class, Account, and a child class, SavingsAccount.
# Task 1
# 
# 👉 Implement properties as instance variables, and set them to None or 0.
# 
# Account has the following properties:
# 
#     • title
#     • Balance
# SavingsAccount has the following properties:
# 
#     • interestRate

# In[41]:


class account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    def print_detail(self):
        return self.title,self.balance

class SavingsAccount(account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate
    def print_detail(self):
        return self.title,self.balance,self.interestRate


# In[42]:


obj1=account("Ashish",5000)
obj1.print_detail()


# In[43]:


obj2=SavingsAccount('Ashish',5000,5)
obj2.print_detail()


# # Challenge 5: Handling a Bank Account

# 🔴 In this challenge, you will define methods for handling a bank account using concepts of inheritance.
# 
# Problem statement
# 
# In this challenge, we will be extending the previous challenge and implementing methods in the parent class and its corresponding child class.
# 
# The initializers for both classes have been defined for you.
# 
# Task 1
# 
# In the Account class, implement the getBalance() method that returns balance.
# 
# Task 2
# 
# In the Account class, implement the deposit(amount) method that adds amount to the balance.
# 
# It does not return anything.
# 
# Task 3
# 
# In the Account class, implement the withdrawal(amount) method that subtracts the amount from the balance.
# 
# It does not return anything.
# 
# Task 4
# 
# In the SavingsAccount class, implement an interestAmount() method that returns the interest amount of the current balance.

# In[76]:


class Account:
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance
    def get_balance(self):
        return self.balance
    def deposit(self,amount):
        self.balance+=amount
    def Withdrawal(self,w_amount):
        if w_amount<self.balance:
            self.balance-=w_amount
        else:
            return 'Insufficient Balance'
class Saving_Account(Account):
    def __init__(self,title,balance,intrestrate):
        super().__init__(title,balance)
        self.intrestrate=intrestrate
    def intrestamount(self):
        return self.balance*(self.intrestrate/100)


# In[79]:


obj5=Account('sachin',2000)
print(f'Balance is {obj5.get_balance()}')
obj5.deposit(500)
print(f'The new balance after deposit {obj5.get_balance()}')
obj5.Withdrawal(1000)
print(f'The new balance after withdraw {obj5.get_balance()}')
obj6=Saving_Account('sachin',2000,5)
print(f'The intrest amount is {obj6.intrestamount()}')

