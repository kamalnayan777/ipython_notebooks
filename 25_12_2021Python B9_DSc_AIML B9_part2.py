#!/usr/bin/env python
# coding: utf-8

# # Property Decorators - Getters, Setters, and Deleters

# In[8]:


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
    def fullName(self):
        return f"{self.first} {self.last}"


# In[9]:


emp_1 = Employee("Kamal","Seth",100000)
emp_1.email


# In[12]:


emp_1.email ='kamal.123@gmail.com'


# In[16]:


emp_1.email


# In[ ]:


# update the Email Automatically once first or last name changes


# In[25]:


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    def email(self):
        return f"{self.first}.{self.last}.@gmail.com"
    def fullName(self):
        return f"{self.first} {self.last}"
    


# In[26]:


emp_1 = Employee("Kamal","Seth",100000)
emp_1.email
# in above  case where we added function email ,we need to call with
# email() so if somebody called it with only email like first example
# they need to change the code
# so @property decorator makes function to be called as variable 


# In[21]:


emp_1.email() ='kamal.123@gmail.com'


# In[28]:


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    # access like attr and define as a method
    @property
    def email(self):
        return f"{self.first}.{self.last}.@gmail.com"
    def fullName(self):
        return f"{self.first} {self.last}"
    


# In[ ]:





# In[29]:


emp_1 = Employee("Kamal","Seth",100000)
emp_1.fullName()


# In[38]:


emp_1.email='kamal.123@gmail.com'


# In[40]:


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    # access like attr and define as method
    @property
    def email(self):
        return f"{self.first}.{self.last}.@gmail.com"
    @property
    def fullName(self):
        return f"{self.first} {self.last}"


# In[45]:


emp_1 = Employee("Niteesh","Vanama",100000)
print (emp_1.email)
print (emp_1.fullName)


# In[46]:


print (emp_1.first)
print (emp_1.last)


# In[49]:


# now i want to change full name  which will change first last
emp_1.fullName ="Jeff Bridge"


# In[ ]:


# use setter for this


# In[67]:


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    # access like attr and define as method
    @property
    def email(self):
        return f"{self.first}.{self.last}.@gmail.com"
    @property
    def fullName(self):
        return f"{self.first} {self.last}"
    
    @fullName.setter
    def fullName(self,name):
        first ,last   = name.split(' ')
        self.first = first
        self.last  =last
    
        
        


# In[ ]:





# In[68]:


emp_1 = Employee("Kamal","Seth",400000)
emp_1.email
emp_1.last


# In[69]:


emp_1.first


# In[70]:


emp_1.fullName


# In[71]:


emp_1.fullName ="avv Bridge"


# In[72]:


emp_1.email


# In[73]:


emp_1.first


# In[74]:


emp_1.last


# In[76]:


emp_1.fullName


# In[149]:


# another usage of setter
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
#         self.base =  int(self.pay/3)
        self.basePay = int(self.pay/3)
        self.pfContro  = int(self.pay/10)
        
    # access like attr and define as method
    @property
    def basePay_pfContro(self):
        return  self.basePay , self.pfContro

    
    @property
    def email(self):
        return f"{self.first}.{self.last}.@gmail.com"
    
    @property
    def fullName(self):
        return f"{self.first} {self.last}"
    
    @fullName.setter
    def fullName(self,name):
        first ,last   = name.split(' ')
        self.first = first
        self.last  =last
        
    @basePay_pfContro.setter
    def basePay_pfContro(self,pay):
        self.basePay = int(pay)/3
        self.pfContro  = int(pay)/10
    
    
    


# In[143]:


emp_2 = Employee('Shradha','Kute',100000)


# In[144]:


emp_2.__dict__


# In[145]:


emp_2.basePay_pfContro


# In[146]:


emp_2.pay


# In[147]:


emp_2.basePay_pfContro  = 130000


# In[148]:


emp_2.__dict__


# In[150]:


emp_2.basePay_pfContro =140000


# In[151]:


emp_2.__dict__


# # ignore for this lecture
# # below is for next lecture 

# In[ ]:





# # Decorators - Dynamically Alter The Functionality Of Your Functions
# 

# In[ ]:





# In[64]:


def sum_numbers(num1, num2, num3):
    return num1+num2+num3


# In[65]:


a = sum_numbers(1,2,3)
b= sum_numbers(4,2,2)


# In[67]:


print(a)


# In[70]:


a+b


# In[71]:


6+8


# In[ ]:





# In[76]:


def outer_function():
    msg ="Bye"
    def inner_function():
        print (msg)
    return inner_function()
outer_function()


# In[ ]:





# In[91]:


def make():
    pass
make()


# In[79]:


def outer_function():
    msg ="Hi"
    def inner_function():
        print (msg)
    return inner_function
outer_function()


# In[96]:


def outer_function():
    msg ="HEY"
    def inner_function():
        print (msg)
    return inner_function


# In[95]:


my_func = outer_function()


# In[92]:


my_func


# In[93]:


my_func()


# In[ ]:





# In[ ]:





# In[111]:


def outer_function(message):
    msg =message
    def inner_function():
        print (msg)
    return inner_function


# In[100]:


outer_function("Hi Man")


# In[112]:


hi_func = outer_function('Hi There')
bye_func =outer_function("Bye for Now")


# In[113]:


bye_func


# In[114]:


hi_func()


# In[115]:


bye_func()


# In[ ]:


# same


# In[116]:


def outer_function(message):
    def inner_function():
        print (message)
    return inner_function


# In[117]:


hi_func = outer_function('Hi There')
bye_func =outer_function("Bye for Now")


# In[118]:


bye_func()


# In[ ]:


# Decorator  -->function that takes another functions as an  argument


# In[119]:


0 1 1 2 3 5 8 13 21


# In[120]:


def fibo(n):
    if n<=0:
        return "Wrong Input"
    elif n ==1 :
        return 1
    elif  n==2 :
        return 2
    else :
        return fibo(n-1)+fibo(n-2)


# In[125]:


fibo(7)


# In[126]:


# fibo(6)+fibo(5)
# fibo(5)+fibo(4)  + fibo(4)+fibo(3)
# fibo(4)+fibo(3) + fibo(3)+fibo(2) +  fibo(3)+fibo(2) + fibo(2)+fibo(1)
# fibo(3)+fibo(2) +   fibo(2)+fibo(1) +  fibo(2)+fibo(1) + 2 + fibo(2)+fibo(1) + 2 + 2+1
#  2+1 + 2 + 2+ 1+2+1 +2 +2 +1 +2+2+1


# In[ ]:




