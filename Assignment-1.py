#!/usr/bin/env python
# coding: utf-8

# In[41]:


# Write a Python program to get the Fibonacci series between 0 to 50
def fib(n):
    fib_series = [0, 1]
    for i in range(1, n):
        next_number = fib_series[-1] + fib_series[-2]
        fib_sequence.append(next_number)
    return fib_sequence

print(fibonacci(10))


# In[52]:


# Write a Python program that accepts a word from the user and reverse it.
name='Edyoda'
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

