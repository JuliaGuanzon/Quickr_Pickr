#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import data libraries to read date range for stock ticker historical data range
from datetime import date, timedelta


# In[2]:


def get_begin_date(curr_date, duration):
    return curr_date - timedelta(duration)


# In[ ]:




