#!/usr/bin/env python
# coding: utf-8

# In[26]:


# Write a Python program to get the Fibonacci series between 0 to 50
fib_series = [0,1]
new_num=1
while True:
    new_num=fib_series[-1]+fib_series[-2]
    if new_num>50:
        break
    fib_series.append(new_num)
print(fib_series)


# In[27]:


# Write a Python program that accepts a word from the user and reverse it.
name=input('enter the name to revers')
rev_name=""
for alpha in range(len(name)-1,-1,-1):
    rev_name+=name[alpha]
print(rev_name)


# In[5]:


# Write a Python program to count the number of even and odd numbers from a series of numbers.
numbers=(1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count=0
odd_count=0
for i in numbers:
    if i%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print('Count of even numbers is:',even_count)
print('Count of odd numbers is:',odd_count)

