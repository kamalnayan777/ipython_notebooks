#!/usr/bin/env python
# coding: utf-8

# In[57]:


# web crawling using requests, bs4


# # What Is Web Scraping?
# Web scraping is the process of gathering information from the Internet. Even copying and pasting the lyrics of your favorite song is a form of web scraping! However, the words “web scraping” usually refer to a process that involves automation. Some websites don’t like it when automatic scrapers gather their data, while others don’t mind.
# 
# If you’re scraping a page respectfully for educational purposes, then you’re unlikely to have any problems. Still, it’s a good idea to do some research on your own and make sure that you’re not violating any Terms of Service before you start a large-scale project.

# In[60]:


import requests


# In[61]:


requests.get('https://api.github.com')


# In[62]:


response = requests.get('https://api.github.com')


# In[63]:


response.status_code


# In[64]:


if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')


# In[65]:


if response:
    print('Success!')
else:
    print('An error has occurred.')


# In[66]:


response = requests.get('https://api.github.com')


# In[73]:


response.content


# In[72]:


response.text


# In[75]:


response.encoding = 'utf-8'


# In[76]:


response.text


# In[79]:


import pprint


# In[83]:


pprint.pprint(response.headers,indent = 3)


# In[84]:


response.headers['Content-Type']


# In[16]:


from getpass import getpass


# In[85]:


requests.get('https://api.github.com/user', auth=('username', getpass()))


# In[86]:


requests.get('https://api.github.com/user')


# In[87]:


URL = "https://www.msn.com/en-in/news/other/earthquake-strikes-near-bengaluru-normal-life-not-affected/ar-AAS2BpO?ocid=BingNewsSearch"
page = requests.get(URL)


# In[88]:


page.text


# In[89]:


page.content


# In[96]:


import requests
from bs4 import BeautifulSoup

URL = "https://www.msn.com/en-in/news/other/earthquake-strikes-near-bengaluru-normal-life-not-affected/ar-AAS2BpO?ocid=BingNewsSearch"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
soup


# In[106]:


content  = soup.find(name='meta')
content
# dir(content)


# In[117]:


for each_div in soup.find_all('div'):
    print (each_div.text)
    


# In[112]:


results = soup.find(id="msnewsroot")
results


# In[35]:


print(results.prettify())


# In[118]:


soup.prettify()


# In[136]:


[link.text for link in soup.find_all("a")]


# In[140]:


soup.find_all("h3")


# In[141]:


import webbrowser


# In[142]:


webbrowser.open('http://bing.com') 


# In[147]:


webbrowser.open('http://bing.com')


# In[ ]:




