#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Write a python function to sum all the number is a list
def sum_list(list1):
    sum_tot=0
    for element in list1:
        sum_tot+=element
        statment='+'.join(map(str,list1))
    return(f"{statment} =",sum_tot)
list_a=list(map(int,input("Enter the numbers:").split()))
sum_list(list_a)


# In[123]:


# Write a python program to reverse the string
def revers_string(word):
    for i in range(len(word)-1,-1,-1):
        print(word[i],end="")
word1=input("Enter the word that need to revers: ")
revers_string(word1)


# In[3]:


# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def upper_lower_number(word):
    upper_count=0
    lower_count=0
    for char in word:
        if char.isupper():
            upper_count+=1
        elif char.isspace():
            continue
        else:
            lower_count+=1
    print("The number of upper case letters are",upper_count)
    print("The number of lower case letters are",lower_count)

word=input("Enter the sentence: ")
upper_lower_number(word)


# In[ ]:




