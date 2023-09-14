#!/usr/bin/env python
# coding: utf-8

# In[132]:


class Restaurant:
    # Consider admin Email id=admin@Akshaya.com and Password as=AKSHAYA_PATRA
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
        
        elif self.Email_Id in Restaurant.user_details and self.Enter_password == Restaurant.user_details[self.Email_Id]['password']:
            print('\033[93m'+'Welcom')
            self.Menu_user()
        
        elif self.Email_Id not in Restaurant.user_details:
            print('\033[91m'+'User not found in Database!....Please register')
            self.Email_Id=input('Enter your email_id:')
            self.Enter_password_1=input('Enter new password:')
            self.Enter_password_2=input('Enter same password again:')
            self.name_user=input('Enter the name of the user:')
            self.Cantact_number=input('Enter the Contact_number of the user:')
            self.user_Adress=input('Enter full present adress with door number:')
            if self.Enter_password_1==self.Enter_password_2:
                self.user_detail_temp={'password':self.Enter_password_1,'User_name':self.name_user,'Cantact_number':self.Cantact_number,'Adress':self.user_Adress}
                Restaurant.user_details[self.Email_Id]=self.user_detail_temp
                print('Rigestration succesful','\n','Login now')
                self.login()
            else:
                print('\033[98m'+'Please entered are not matching please Enter same password two times')
                self.Enter_password_1=input('Enter new password:')
                self.Enter_password_2=input('Enter same password again:')
                if self.Enter_password_1==self.Enter_password_2:
                    self.user_detail_temp={'password':self.Enter_password_1,'User_name':self.name_user,'Cantact_number':self.Cantact_number,'Adress':self.user_Adress}
                    Restaurant.user_details[self.Email_Id]=self.user_detail_temp
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
        elif self.Email_Id in Restaurant.user_details and self.Enter_password == Restaurant.user_details[self.Email_Id]['password']:
            print('Login succesful!')
            self.Menu_user()
        elif self.Email_Id in Restaurant.user_details and self.Enter_password != Restaurant.user_details[self.Email_Id]['password']:
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
            self.Qty_per_pack=int(input('Enter the Qty in numbers:'))
            self.unit=input('Enter unit of measurment:')
            self.price=int(input('The cost for one pack:'))
            self.Discount=int(input('Enter the discount:'))
            self.stock=int(input('Stock available in number:'))
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
            self.FoodID=input('Enter the food ID that need to change:')
            if self.FoodID in Restaurant.Food_available:
                Restaurant.Food_available[self.FoodID]['Name']=input('Enter the name of new item:')
                Restaurant.Food_available[self.FoodID]['Quantity per pack']['value']=int(input('Enter the Qty of new item:'))
                Restaurant.Food_available[self.FoodID]['Quantity per pack']['unit']=input('Enter the unit:')
                Restaurant.Food_available[self.FoodID]['Price']=int(input('Enter new price:'))
                Restaurant.Food_available[self.FoodID]['Discount']=int(input('Enter the revised Discount:'))
                Restaurant.Food_available[self.FoodID]['Stock']=int(input('Enter total stock available:'))
            else:
                print("Food id provided is not available, Please provide valid id")
        else:
            print('Please login again')
    
    def Delete_food_using_ID(self):
        if self.Email_Id=='admin@Akshaya.com' and self.Enter_password=='AKSHAYA_PATRA':
            self.FoodID=input('Enter the food ID that need to change:')
            if self.FoodID in Restaurant.Food_available:
                del Restaurant.Food_available[self.FoodID]
            else:
                print("Food id provided is not available, Please provide valid id")
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
        self.temp=[]
        for key in Restaurant.Food_available:
            self.place_new_order_list=Restaurant.Food_available[key]['Name'],(Restaurant.Food_available[key]['Quantity per pack']['value'],Restaurant.Food_available[key]['Quantity per pack']['unit'],'per plate',Restaurant.Food_available[key]['Price'])
            self.temp.append(self.count_3,'-->',self.place_new_order_list)
            self.count_3+=1
        print(self.temp)
            
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


# In[134]:


admin=Restaurant()
admin.Start()


# In[135]:


admin.get_Menu_admin_details()


# In[136]:


admin.Edit_food_using_ID()


# In[137]:


admin.get_Menu_admin_details()


# In[138]:


admin.Delete_food_using_ID()


# In[139]:


admin.get_Menu_admin_details()


# In[141]:


user_1=Restaurant()
user_1.Start()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




