#!/usr/bin/env python
# coding: utf-8

# In[20]:


# Write a python program to creat a lambda function that adds 25 to a given number passed in as an arguments
num=int(input("Enter the number:"))
total=lambda num:num+25
print(total(num))


# In[30]:


# Write a Python program to triple all numbers of a given list of integers. Use Python map.
list1=list(map(int,input("Enter the number").split()))
print('The original list is:',list1)
triple=list(map(lambda x:x*3,list1))
print('The list after tripling:',triple)


# In[32]:


# Write a Python program to square the elements of a list using map() function.
list_initial=list(map(int,input("enter the number").split()))
print('The original list is:',list_initial)
squar=list(map(lambda x:x**2,list_initial))
print('The list after Squar:',squar)

