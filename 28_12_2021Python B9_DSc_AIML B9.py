#!/usr/bin/env python
# coding: utf-8

# # Decorators

# Before you can understand decorators, you must first understand how functions work. For our purposes, a function returns a value based on the given arguments. Here is a very simple example:
# 
# 

# In[2]:


def add_one(number):
    return number + 1

add_one(2)


# #First-Class Objects
# 
# In Python, functions are first-class objects. This means that functions can be passed around and used as arguments, just like any other object (string, int, float, list, and so on). Consider the following three functions:

# In[12]:


def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, all good !"

def greet_bob(greeter_func):
    return greeter_func("kamal seth 123")


# In[ ]:





# In[4]:


say_hello('kamal ')


# In[5]:


be_awesome('kamal ')


# In[10]:


greet_bob(say_hello)


# In[11]:


greet_bob(be_awesome)


# Note that greet_bob(say_hello) refers to two functions, but in different ways: greet_bob() and say_hello. The say_hello function is named without parentheses. This means that only a reference to the function is passed. The function is not executed. The greet_bob() function, on the other hand, is written with parentheses, so it will be called as usual.
# 
# 

# # inner function

# In[14]:


def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()


# In[17]:


parent()


# Returning Functions From Functions
# 

# In[19]:


def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child


# In[20]:


first = parent(1)


# In[21]:


second = parent(2)


# In[22]:


first


# In[23]:


second


# In[24]:


first()


# In[25]:


second()


# # Simple Decorators
# 
# Now that you’ve seen that functions are just like any other object in Python, you’re ready to move on and see the magical beast that is the Python decorator. Let’s start with an example:
# 
# 

# In[27]:


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")


# In[28]:


say_whee = my_decorator(say_whee)


# In[29]:


say_whee


# In[30]:


say_whee()


# To understand what’s going on here, look back at the previous examples. We are literally just applying everything you have learned so far.
# 
# The so-called decoration happens at the following line:

# In[31]:


say_whee = my_decorator(say_whee)


# In effect, the name say_whee now points to the wrapper() inner function. Remember that you return wrapper as a function when you call my_decorator(say_whee):

# In[32]:


say_whee


# In[42]:


from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 20:
            func()
        else:
            print('NO PARTY')  # Hush, the neighbors are asleep
    return wrapper

def say_whee1():
    print("Whee! its not night !!!! party time")


# In[43]:


say_whee1 = not_during_the_night(say_whee1)


# In[44]:


say_whee1


# In[45]:


say_whee1()


# In[54]:


@not_during_the_night
def say_whee1():
    print("Whee! its not night !!!! party time")
say_whee1()


# # Syntactic Sugar!
# 
# The way you decorated say_whee() above is a little clunky. First of all, you end up typing the name say_whee three times. In addition, the decoration gets a bit hidden away below the definition of the function.
# 
# Instead, Python allows you to use decorators in a simpler way with the @ symbol, sometimes called the “pie” syntax. The following example does the exact same thing as the first decorator example:

# In[50]:


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


# In[52]:


@my_decorator
def say_whee2():
    print("Whee2 !")
say_whee2()


# So, @my_decorator is just an easier way of saying say_whee = my_decorator(say_whee). It’s how you apply a decorator to a function.

# # Reusing Decorators
# Recall that a decorator is just a regular Python function. All the usual tools for easy reusability are available. Let’s move the decorator to its own module that can be used in many other functions.

# In[ ]:


# Create a file called decorators.py with the following content:


# In[55]:


import os
os.getcwd()


# In[ ]:





# In[56]:


from decorator_lu import do_twice


# In[ ]:





# In[59]:


@do_twice
def say_whee():
    print("Whee! thrice ")


# In[60]:


say_whee()


# # Decorating Functions With Arguments
# Say that you have a function that accepts some arguments. Can you still decorate it? Let’s try:

# In[68]:


@do_twice
def greet(name):
    print(f"Hello {name}")


# In[69]:


greet('World')


# The problem is that the inner function wrapper_do_twice() does not take any arguments, but name="World" was passed to it. You could fix this by letting wrapper_do_twice() accept one argument, but then it would not work for the say_whee() function you created earlier.
# 
# The solution is to use *args and **kwargs in the inner wrapper function. Then it will accept an arbitrary number of positional and keyword arguments. Rewrite decorators.py as follows:

# In[63]:


from decorator_lu1 import do_twice


# In[ ]:


from importlib import reload  # Python 3.4+
reload(do_twice)


# In[73]:


@do_twice
def greet(name):
    print(f"Hello {name}")


# In[66]:


say_whee()


# In[74]:


greet("Kamal")


# # Returning Values From Decorated Functions
# What happens to the return value of decorated functions? Well, that’s up to the decorator to decide. Let’s say you decorate a simple function as follows:

# In[75]:


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


# In[76]:


hi_adam = return_greeting("Adam")


# In[77]:


print(hi_adam)


# Oops, your decorator ate the return value from the function.
# 
# Because the do_twice_wrapper() doesn’t explicitly return a value, the call return_greeting("Adam") ended up returning None.
# 
# To fix this, you need to make sure the wrapper function returns the return value of the decorated function. Change your decorators.py file:

# In[ ]:


return_greeting("Adam")


# In[78]:


from decorator_lu2 import do_twice


# In[81]:


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


# In[82]:


hi_adam = return_greeting("Adam")


# In[83]:


print(hi_adam)


# In[87]:


import os 


# In[88]:


os.getcwd()


# In[89]:


from os import getcwd


# In[90]:


getcwd()


# In[91]:


from datetime import datetime


# In[92]:


from os import os 


# In[93]:


import os 


# In[94]:


from os import *


# In[98]:


from os import getcwd  as get_cur , chmod as g


# In[96]:


from os import getcwd as f 


# In[97]:


f()


# In[100]:





# In[ ]:




