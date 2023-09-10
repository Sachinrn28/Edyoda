#!/usr/bin/env python
# coding: utf-8

# In[100]:


class Restaurant:
    user_details={'admin@Akshaya.com':'AKSHAYA_PATRA'}
    Food_available={}
    ordered_items={}
    
    def __init__(self):
        print('\033[96m'+'Welcom to our AKSHAYA PATRA Restaurant','\n',"Please Login")
        self.Email_Id=None
        self.Enter_password=None
        self.count=0
        self.count_2=0
        self.order_id=None
        self.count_3=1
    
    def Start(self):
        print('Please Enter your credentials')
        self.Email_Id=input('Enter your email_id:')
        self.Enter_password=input('Enter new password:')
        self.Rigester_user()
        
    def Rigester_user(self):
        if self.Email_Id=='admin@Akshaya.com' and self.Enter_password=='AKSHAYA_PATRA':
            print('\033[93m'+'Admin login succesful')
            self.Menu_admin()
            
        elif self.Email_Id=='admin@Akshaya.com' and self.Enter_password!='AKSHAYA_PATRA':
            print('\033[93m'+'Password not correct, try again')
            self.Start()
        
        elif self.Email_Id in Restaurant.user_details and self.Enter_password == Restaurant.user_details[self.Email_Id]:
            print('\033[93m'+'Welcom')
            self.Menu_user()
        
        elif self.Email_Id not in Restaurant.user_details:
            print('\033[91m'+'User not found in Database!....Please register')
            self.Email_Id=input('Enter your email_id:')
            self.Enter_password_1=input('Enter new password:')
            self.Enter_password_2=input('Enter same password again:')
            self.name_user=input('Enter the name of the user:')
            self.Cantact_number=int(input('Enter the Contact_number of the user:'))
            self.user_Adress=input('Enter full present adress with door number:')
            if self.Enter_password_1==self.Enter_password_2:
                Restaurant.user_details[self.Email_Id]['password']=self.Enter_password_1
                Restaurant.user_details[self.Email_Id]['User_name']=self.name_user
                Restaurant.user_details[self.Email_Id]['Cantact_number']=self.Cantact_number
                Restaurant.user_details[self.Email_Id]['Adress']=self.user_Adress
                print('Rigestration succesful','\n','Login now')
                self.login()
            else:
                print('\033[98m'+'Please enter valid password')
                self.Enter_password_1=input('Enter new password:')
                self.Enter_password_2=input('Enter new password:')
                if self.Enter_password_1==self.Enter_password_2:
                    Restaurant.user_details[self.Email_Id]['password']=self.Enter_password_1
                    Restaurant.user_details[self.Email_Id]['User_name']=self.name_user
                    Restaurant.user_details[self.Email_Id]['Cantact_number']=self.Cantact_number
                    Restaurant.user_details[self.Email_Id]['Adress']=self.user_Adress
                    print('Rigestration succesful','\n','Login now')
                    self.login()
                else:
                    print("You have entered maximum trial!, Please try later")
                    self.Rigester_user()

    
    def login(self):
        self.Email_Id=input('Enter Email_Id:')
        self.Enter_password=input('Enter the password:')
        self.count+=1
        if self.Email_Id not in Restaurant.user_details:
            print('Email not found!.... please creat user')
        elif self.Email_Id in Restaurant.user_details and self.Enter_password == Restaurant.user_details[self.Email_Id]:
            print('Login succesful!')
        elif self.Email_Id in Restaurant.user_details or self.Enter_password != Restaurant.user_details[self.Email_Id]:
            print('Password not correct! try again')
            if self.count<3:
                self.login()
            else:
                print('You reached maximun trial!, Please try after some time')
                
    def Menu_admin(self):
        self.count_2+=1
        self.n=int(input('Enter how many type of food available:'))
        for i in range(0,self.n):
            self.FoodID='APFID'+str(self.count)
            self.Food_name=input('Enter the food name:')
            self.Qty_per_pack=int(input('Enter the Qty:'))
            self.unit=input('Enter of measurment:')
            self.price=int(input('The cost for one pack:'))
            self.Discount=int(input('Enter the discount:'))
            self.stock=int(input('Stock available:'))
            self.Food_details={'Name':self.Food_name,'Quantity per pack':{'value':self.Qty_per_pack,'unit':self.unit},'Price':self.price,'Discount':self.Discount,'Stock':self.stock}
            Restaurant.Food_available[self.FoodID]=self.Food_details
            self.count+=1
    
    def get_Menu_admin_details(self):
        if self.Email_Id=='admin@Akshaya.com' and self.Enter_password=='AKSHAYA_PATRA':
            print(Restaurant.Food_available)
        else:
            print('Please login again')
            
    def Edit_food_using_ID(self):
        if self.Email_Id=='admin@Akshaya.com' and self.Enter_password=='AKSHAYA_PATRA':
            Restaurant.self.FoodID=input('Enter the food ID that need to change:')
            Restaurant.self.Food_availabl[self.FoodID]['Name']=input('Enter the name of new item:')
            Restaurant.self.Food_availabl[self.FoodID]['Quantity per pack']['value']=int(input('Enter the Qty of new item:'))
            Restaurant.self.Food_availabl[self.FoodID]['Quantity per pack']['unit']=input('Enter the unit:')
            Restaurant.self.Food_availabl[self.FoodID]['Price']=int(input('Enter new price:'))
            Restaurant.self.Food_availabl[self.FoodID]['Discount']=int(input('Enter the revised Discount:'))
            Restaurant.self.Food_availabl[self.FoodID]['Stock']=int(input('Enter total stock available:'))
        else:
            print('Please login again')
    
    def Delete_food_using_ID(self):
        if self.Email_Id=='admin@Akshaya.com' and self.Enter_password=='AKSHAYA_PATRA':
            Restaurant.self.FoodID=input('Enter the food ID that need to change:')
            del Restaurant.self.Food_availabl[self.FoodID]
            
    def Menu_user(self):
        print(''' 
        Please select the option
        1. Place new order
        2. order History
        3. update profile''')
        self.Menu_user_entry=int(input('Select options from above:'))
        if self.Menu_user_entry==1:
            self.place_new_order()
        elif self.Menu_user_entry==2:
            self.order_history()
        elif self.Menu_user_entry==3:
            self.update_profile()
        elif self.Menu_user_entry>3:
            print('Please select a valid option')
    def place_new_order(self):
        for food_list in Restaurant.Food_available:
            print(self.count_3,'for',Restaurant.Food_available[food_list]['Name'])
            self.count_3+=1   
        else:
            print('Please enter valid option:')
        
    def order_history(self):
        print(Restaurant.Food_available)
    
    def update_profile(self):
        # Email id changing pending
        Restaurant.user_details[self.Email_Id]['User_name']=input('Enter the name that need to change :')
        Restaurant.user_details[self.Email_Id]['Cantact_number']=int(input('Enter the contact number:'))
        Restaurant.user_details[self.Email_Id]['Adress']=input('Enter the name that need to change :')
        self.old_password=input('PLease type old password:')
        if self.old_password==Restaurant.user_details[self.Email_Id]['password']:
            Restaurant.user_details[self.Email_Id]['password']=input('Enter new password')
        else:
            print('password not matching')


# In[102]:


user_2=Restaurant()
user_2.Start()


# In[103]:


user_2.get_Menu_admin_details()


# In[104]:


user_2=Restaurant()
user_2.Start()


# In[ ]:




