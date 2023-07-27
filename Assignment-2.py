#!/usr/bin/env python
# coding: utf-8

# In[1]:


# write a python program to get a list, stored in increasing order by the last element in each tuple from a given list of non empty tuple.
samp=[(2,5),(1,2),(4,4),(2,3),(2,1)]
for i in range(len(samp)):
    min_index=i
    for j in range(i+1,len(samp)):
        if samp[j][-1]<samp[min_index][-1]:
            min_index=j
        samp[i],samp[min_index]=samp[min_index],samp[i]
print(samp)


# In[18]:


# Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values
dict = {}
for letter in range(ord('a'), ord('z')+1):
    ascii_dict[chr(letter)] = letter
print(ascii_dict)

