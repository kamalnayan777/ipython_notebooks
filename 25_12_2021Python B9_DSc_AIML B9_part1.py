#!/usr/bin/env python
# coding: utf-8

# In[1]:


# libraries in python 
def sum_2_number(a,b):
    return a+b 


# In[3]:


sum_2_number(3,4)


# In[4]:


import os


# In[5]:


os.getcwd()


# In[9]:


import intro


# In[12]:


from importlib import reload


# In[20]:


reload(intro)


# In[15]:


help(intro)


# In[16]:


intro.introduce('kamal','30','MCA')


# In[19]:


intro.introduce('abc','31','BTech')


# In[21]:


intro.sum_2_num(5,6)


# In[22]:


from datetime import datetime


# In[27]:


import str_date


# In[24]:


str_date.convert_string_date('Jun 1 2005  1:33PM')


# In[26]:


str_date.convert_string_date('Dec 24 2021 4:33PM')


# In[33]:


reload(str_date)


# In[34]:


help(str_date)


# In[43]:


from str_date import convert_string_date2


# In[42]:


reload(str_date)


# In[44]:


convert_string_date2('12-12-2019')


# # recap of OOPS

# In[53]:


class Simple:
    '''
    doc of simple class
    '''
    pass


# In[48]:


class Simple_1(object):
    pass


# In[49]:


type(Simple)


# In[50]:


type(Simple_1)


# In[58]:


Simple.__doc__


# In[59]:


Simple.__dict__


# In[64]:


Simple.firstName ='Kamal'


# In[74]:


Simple.__dict__


# In[66]:


Simple.lastName ='Seth'


# In[68]:


Simple.emailId = Simple.firstName+'.'+Simple.lastName+'@gmail.com'


# In[70]:


Simple.emailId


# In[72]:


Simple.firstName ='Jackson'


# In[73]:


Simple.emailId


# In[103]:


class Simple(object):
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.emailId = self.firstName+'.'+        self.lastName+'@gmail.com'
        
    
    


# In[102]:


Simple('kamal','seth')


# In[88]:


Simple('kamal','seth').__dict__


# In[84]:


Simple('kamal','seth').firstName


# In[85]:


Simple('kamal','seth').lastName


# In[89]:


Simple('jackson','seth').__dict__


# In[96]:


inst_1 = Simple('lets','upgrade1')


# In[92]:


inst_1.__dict__


# In[93]:


type(Simple)


# In[94]:


type(inst_1)


# In[97]:


inst_1.emailId


# In[99]:


inst_2 = Simple('abc','upgrade1')


# In[100]:


inst_2.__dict__


# In[110]:


class Simple(object):
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.emailId = self.firstName+'.'+        self.lastName+'@gmail.com'
        
    def introduce_me(self):
        return f"{self.firstName} {self.emailId}"
    
    


# In[112]:


inst_3 = Simple('Kamal','Seth')


# In[116]:


inst_3.introduce_me()


# In[ ]:





# In[ ]:




