#!/usr/bin/env python
# coding: utf-8

# In[3]:


# import data libraries to read date range for stock ticker historical data range
# from datetime import date, timedelta
from datetime import *


# In[6]:


def get_begin_date(curr_date, duration):
    return curr_date - timedelta(duration)


# In[7]:


def get_present_time():
    now_1 = datetime.now()
    return now_1.strftime("%H:%M:%S")


# In[ ]:




