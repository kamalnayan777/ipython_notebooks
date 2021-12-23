#!/usr/bin/env python
# coding: utf-8
"""
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
"""
# In[1]:


# [1(211),2(212),3(213),4(214),5(215)....]


# In[3]:


a = [1,2,3]
a


# In[4]:


b = a


# In[18]:


a


# In[17]:


a.append(102)


# In[19]:


b


# In[13]:


id(a)


# In[14]:


id(b)


# In[21]:


id(c)


# In[15]:


c = b


# In[20]:


c


# In[74]:


print (b)


# In[22]:


from copy import deepcopy


# In[23]:


a = [1,2,3]
b= deepcopy(a)

# a.append(8)


# In[27]:


a


# In[26]:


a.append(67)


# In[28]:


print (b)


# In[29]:


id(a)


# In[30]:


id(b)


# In[ ]:





# In[31]:


print(id(a))
print (id(b))


# In[32]:


a = 'kamal'


# In[33]:


b=a


# In[37]:


a


# In[38]:


b


# In[36]:


a+=' lets'


# In[39]:


id(a)


# In[40]:


id(b)


# In[41]:


a = (1,2,3)
b=a


# In[54]:


id(a)


# In[55]:


id(b)


# In[47]:


a = (1,2,[])


# In[48]:


b= a


# In[51]:


a[2].append(45)


# In[52]:


a


# In[53]:


b


# In[57]:


a = {
    'name':'kamal'
}


# In[58]:


b = a


# In[59]:


id(a)


# In[60]:


id(b)


# In[62]:


a['class'] ='Python'


# In[63]:


a


# In[64]:


b


# In[ ]:





# # collections 

# # Counter
# defaultdict
# OrderedDict
# deque
# ChainMap
# namedtuple

# In[65]:


totalItems = [1,4,3,5,7,3,1,8,5,3,5,8,5,9,7,3,9,4,6,3,2,9,9]


# In[66]:


for i in totalItems:
    print (f" {i} occured : {totalItems.count(i)} times ")


# In[67]:


{i:totalItems.count(i) for i in totalItems}#  dict iteration /comp 


# In[68]:


from collections import Counter


# In[75]:


print (Counter(totalItems))
# c = Counter(totalItems)


# In[76]:


c


# In[89]:


print (Counter({1:3,2:4}))


# In[78]:


# cnt = Counter({1:3,2:4})
# print (cnt)
cnt = Counter(totalItems)
print(cnt)


# In[79]:


cnt.most_common(3)


# In[80]:


# read csv
with open('/Users/kamalseth/Downloads/uk-500.csv','r') as f :
    uk = f.readlines()


# In[93]:


uk[0].split(',')[0].strip('""')


# In[103]:


first_names = [each_line.split(',')[0].strip('""') for each_line in uk[1:]]


# In[107]:


f_names  = Counter(first_names)


# In[108]:


f_names.most_common(5)


# In[109]:


last_names = [each_line.split(',')[1].strip('""') for each_line in uk[1:]]


# In[111]:


l_name = Counter(last_names)
l_name.most_common(5)


# In[ ]:





# In[ ]:





# In[112]:


import time


# In[117]:


time.time()


# In[121]:


def my_time(epoch_time):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch_time))


# In[122]:


my_time(time.time())


# In[131]:


start  =time.time()
def hi(a,b):
    list(range(10000000))
hi(2,3)
time.sleep(2)
hi(5,6)
print (f"total : {time.time()-start}")


# # Next Lecture 

# In[15]:


from collections import defaultdict


# In[16]:


nums = defaultdict(int)


# In[17]:


print (nums)


# In[18]:


nums['1']


# In[19]:


print(nums)


# In[26]:


from collections import defaultdict

count = defaultdict(int)
names_list = "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()
for names in names_list:
    count[names] +=1
print(count)


# In[28]:


from collections import OrderedDict


# In[29]:


od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)


# In[30]:


list = ["a","c","c","a","b","a","a","b","c"]
cnt = Counter(list)
od = OrderedDict(cnt.most_common())
for key, value in od.items():
    print(key, value)


# # NEXT is WHAT ????

# # Data Structure 

# In[33]:


x = 5 
if x<6:
    raise Exception('not good')


# In[34]:


from collections import deque


# In[35]:


list = ["a","b","c"]
deq = deque(list)
print(deq)


# In[37]:


deq.append("d")
print (deq)
deq.appendleft("e")
print(deq)


# In[38]:


deq.pop()
print (deq)
deq.popleft()
print(deq)


# In[ ]:





# In[39]:


list = ["a","b","c"]
deq = deque(list)
print(deq)
print(deq.clear())


# # the chain map
# ##ChainMap is used to combine several dictionaries or mappings. It returns a list of dictionaries.
# 
# 

# In[40]:


from collections import ChainMap


# In[41]:


dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
chain_map = ChainMap(dict1, dict2)
print(chain_map.maps)


# In[42]:


print (dict1 | dict2)


# In[43]:


dict2['c'] = 5
print(chain_map.maps)


# In[48]:


issubclass(ChainMap,dict)


# In[50]:


dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
chain_map = ChainMap(dict1, dict2)
print (chain_map.keys())
print (chain_map.values())


# # The namedtuple()
# 
# ## The namedtuple() returns a tuple with names for each position in the tuple. One of the biggest problems with ordinary tuples is that you have to remember the index of each field of a tuple object. This is obviously difficult. The namedtuple was introduced to solve this problem.
# 
# 

# In[51]:


from collections import namedtuple


# In[52]:


Student = namedtuple('Student', 'fname, lname, age')
s1 = Student('John', 'Clarke', '13')
print(s1.fname)


# In[53]:


print (s1)


# In[54]:


s2 = Student._make(['Adam','joe','18'])
print(s2)


# In[55]:


s2 = s1._asdict()
print(s2)


# In[56]:


s2 = s1._replace(age='14')
print(s1)
print(s2)


# # Time Module

# In[57]:


import time


# In[59]:


# UNIX systems define the epoch as January 1, 1970. 
#The Win32 API, on the other hand, defines the epoch as January 1, 1601.
time.gmtime(0)


# In[60]:


time.time()


# In[61]:


# convert epoch to Human redable
time.ctime(time.time())


# In[62]:


time.ctime()


# In[119]:


total =[1,2,3,4,5]


# In[120]:


[id(i) for i in total]


# In[121]:


print (id(total))


# In[122]:


import functools


# In[ ]:





# In[ ]:




