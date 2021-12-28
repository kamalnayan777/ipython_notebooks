#!/usr/bin/env python
# coding: utf-8

# 
# # classmethods and staticmethods

# In[ ]:





# In[ ]:





# In[ ]:





# In[3]:


class Employee:
    num_of_employees = 0
    raise_amount = 1.05 #5%
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_of_employees +=1
        #self.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount) # self.raise_amount
        
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount  = amount
        


# In[1]:


###### important ######
# Regular  methods automatically takes instance as first arugment 
# class methods automatically takes cls as first arugment 
# static methods doesn't pass anything automatically 


# # cls !=class

# In[4]:


emp_1 = Employee("kamal","Seth",100000) # instance 1
emp_2 = Employee("Jack","Wells",120000) # instance 2


# In[11]:


emp_3 = Employee('name','age',140000)


# In[12]:


print (Employee.raise_amount)
print (emp_1.raise_amount)
print (emp_2.raise_amount)
print(emp_3.raise_amount)


# In[ ]:





# In[16]:


# Employee.set_raise_amount(1.10)
Employee.raise_amount = 1.15 #. both are same


# In[17]:


print (Employee.raise_amount)
print (emp_1.raise_amount)
print (emp_2.raise_amount)
print(emp_3.raise_amount)


# In[24]:


emp_3.set_raise_amount(1.2)


# In[25]:


print (Employee.raise_amount)
print (emp_1.raise_amount)
print (emp_2.raise_amount)
print(emp_3.raise_amount)


# In[26]:


emp_1.num_of_employees


# In[27]:


emp_4 = Employee('abc','pqr',455555)


# In[31]:


Employee.num_of_employees


# In[ ]:





# In[32]:


emp_str_1 = "Kamal-Seth-960000"
first ,last ,salary = emp_str_1.split('-')
emp_3 = Employee(first,last,salary)
emp_3.email


# In[35]:


class Employee:
    num_of_employees = 0
    raise_amount = 1.05
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_of_employees +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount) # self.raise_amount
        
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount  = amount
    @classmethod
    def from_string(cls,emp_str):
        first ,last ,salary = emp_str.split('-')
        # alternative constructor
        return cls(first,last,salary)
        # Employee(first,last ,salary)
        
        


# In[36]:


new_emp_2 = Employee("russel-crowe-123000")


# In[37]:


new_emp_1 = Employee.from_string("aman-kac-45555")


# In[40]:


new_emp_1.last


# In[28]:


# static methods 


# In[43]:


class Employee:
    num_of_employees = 0
    raise_amount = 1.05
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_of_employees +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount) # self.raise_amount
        
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount  = amount
    @classmethod
    def from_string(cls,emp_str):
        first ,last ,salary = emp_str.split('-')
        # alternative constructor
        return cls(first,last,salary)
    @staticmethod
    def is_Workday(day):
        if day.weekday()==5 or day.weekday() ==6:
            return False
        
        return True
    
    @staticmethod
    def sum_me(a,b):
        return a+b
        


# In[41]:


from  datetime import date


# In[45]:


Employee.sum_me(11,8)


# In[47]:


date.today().weekday()


# In[50]:


print (Employee.is_Workday(date(2022,1,1)))


# In[51]:


inst_1 = Employee('jack','ryan',999000)
inst_1.email


# In[52]:


inst_2 = Employee.from_string("denzel-wah-89000")
inst_2.email


# In[ ]:





# # Inheritance

# # Subclass

# In[53]:


class Employee:
    num_of_employees = 0
    raise_amount = 1.05
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_of_employees +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount) # self.raise_amount


# In[54]:


class Developer(Employee) :
    pass
    


# In[60]:


class HR(Employee):
    pass


# In[61]:


HR.mro()


# In[58]:


Developer.mro()


# In[62]:


class Dev_Lead(Developer):
    pass


# In[63]:


Dev_Lead.mro()


# In[64]:


d = Developer('Kamal',"Seth",20000)


# In[65]:


d.__dict__


# In[66]:


hr = HR("rashmi","hr",120000)
hr.email


# In[67]:


d.last


# In[68]:


Employee.mro()


# In[69]:


Developer.mro() # method resolution order


# In[70]:


Dev_Lead.mro()


# In[72]:


print (d.pay)
print (d.apply_raise())
print (d.pay)


# In[73]:


class Developer(Employee) :
    raise_amount   = 1.20


# In[74]:


d = Developer('KamalNayan',"Seth",20000)


# In[75]:


d.raise_amount


# In[76]:


print (d.pay)
print (d.apply_raise())
print (d.pay)


# In[77]:


print (Developer.raise_amount)
print (Employee.raise_amount)


# In[81]:


print (d.raise_amount)
print (Employee.raise_amount)


# In[ ]:





# In[82]:


help(Employee)


# In[ ]:





# In[83]:


help(Developer)


# In[85]:


class Developer(Employee) :
    raise_amount =1.10
    def __init__(self , first ,last ,pay ,prog_lang,editor):
        super().__init__(first,last,pay)
        #Employee.__init__(self,first,last,pay) # method 2 

        self.prog_lang = prog_lang
        self.editor = editor
        
    @staticmethod
    def sub_me(a,b):
        return a-b
    


# In[87]:


Developer.sub_me(12,4)


# In[88]:


dev_1 = Developer("kamal","seth",100000,"JS","VSCode")
dev_2 = Developer("jack","Wells",200000,"Python","PyCharm")


# In[89]:


print(dev_1.email  , dev_1.prog_lang, dev_1.editor)


# In[90]:


print(dev_2.email  , dev_2.prog_lang, dev_2.editor)


# In[91]:


Employee.raise_amount


# In[92]:


dev_1.raise_amount


# # STOP HERE ####

# In[57]:


class Manager(Employee):
    def __init__(self , first ,last ,pay ,employees = None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else :
            self.employees  =employees
            
    def add_employee(self,emp):
        if emp not in self.employees :
            self.employees.append(emp)
            
    def remove_employee(self,emp):
        if emp  in self.employees :
            self.employees.remove(emp)
    
    def print_employees(self):
        for emp in self.employees :
            print (f" --> {emp.fullname()}")
            
            
        


# In[95]:


help(super)


# In[58]:


dev_1 = Developer("kamal","seth",100000,"JS")
dev_2 = Developer("jack","Wells",200000,"Python")


# In[59]:


mgr_1 = Manager("Julia","Bagg",80000,[dev_1])


# In[62]:


print (mgr_1.email)
print (mgr_1.print_employees())


# In[63]:


mgr_1.add_employee(dev_2)


# In[64]:


print (mgr_1.print_employees())


# In[65]:


mgr_1.remove_employee(dev_1)


# In[66]:


print (mgr_1.print_employees())


# In[67]:


help(Manager)


# # isinstance issubclass

# In[68]:


isinstance(mgr_1,Manager)


# In[69]:


isinstance(mgr_1,Employee)


# In[70]:


isinstance(mgr_1,Developer)


# In[71]:


issubclass(Employee,Developer)


# In[72]:


issubclass(Developer,Employee)


# In[73]:


issubclass(Manager,Employee)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# 

# In[ ]:




