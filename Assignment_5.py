#!/usr/bin/env python
# coding: utf-8

# 👉 1. Create a JSON file (employee.json) containing employee information of minimum 5 employees. Each employee information consists of Name, DOB, Height, City, State. Write a python program that reads this information from the JSON file and saves the information into a list of objects of Employee class. Finally print the list of the Employee objects.

# In[28]:


import json
employee_information={'employee_1':{'Name':'madhu','DOB':'28-02-1996','city':'mumbai','state':'maharastra'},
                      'employee_2':{'Name':'sachin','DOB':'28-06-1996','city':'chitradurga','state':'karnataka'},
                      'employee_3':{'Name':'sagar','DOB':'20-04-1996','city':'kedarnath','state':'utharkhand'},
                      'employee_4':{'Name':'sooraj','DOB':'01-4-1995','city':'bangalore','state':'karnataka'},
                      'employee_5':{'Name':'ashwathama','DOB':'Tapakeshwara mahadeva temple','city':'karnataka','state':'karnataka'}}
with open("employee.json","w") as file_handler:
    file_handler.write(json.dumps(employee_information))
with open("employee.json","r") as file_handler:
    print(json.load(file_handler))


# 👉 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

# In[37]:


dict_state={'karnataka':'bangalore',
            'maharastra':'mumbai',
            'andrapradesh':'hydrabad',
            'Tamilnadu':'chennai',
           'West bengal':'kolkata',
           'Kerala':'Thirunananthapuram'}
with open('dict_state.json','w') as file_handler:
    file_handler.write(json.dumps(dict_state))
with open('dict_state.json','r') as file_handler:
    print(json.load(file_handler))


# 👉 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:
# 
# 🔴 a. It should have a function ‘description()’ which prints the name and age of the dog.
# 🔴 b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# 🔴 c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
# 🔴 d. Create objects and implement the above functionalities.

# In[52]:


class dog:
    def __init__(self,name,age,coatcolor):
        self.name=name
        self.age=age
        self.coatcolor=coatcolor
    def description(self):
        print('The name of the dog is:',self.name)
        print('The age of the dog is:',self.age)
    def get_info(self):
        print('The coatcolor of the dog is:',self.coatcolor)
class JackRussellTerrier(dog):
    def __init__(self,name,age,coatcolor,gender):
        super().__init__(name,age,coatcolor)
        self.gender=gender
    def description1(self):
        print('The name of the dog is:',self.name)
        print('The age of the dog is:',self.age)
        print('The coatcolor of the dog is:',self.coatcolor)
        print('The gender of the dog is:',self.gender)
class Bulldog(dog):
    def __init__(self,name,age,coatcolor,gender,price):
        super().__init__(name,age,coatcolor)
        self.gender=gender
        self.price=price
    def description2(self):
        print('The name of the dog is:',self.name)
        print('The age of the dog is:',self.age)
        print('The coatcolor of the dog is:',self.coatcolor)
        print('The gender of the dog is:',self.gender)
        print('It cost:',self.price)


# In[46]:


dog_object_1=dog('german shepherd',5,'gray')
dog_object_1.description()
dog_object_1.get_info()


# In[55]:


dog_object_2=JackRussellTerrier('JackRussellTerrier',2,'gray and white','male')
dog_object_2.description1()


# In[62]:


dog_object_3=Bulldog('Bulldog',3,'gray and white','disoster female',120000)
dog_object_3.description2()

