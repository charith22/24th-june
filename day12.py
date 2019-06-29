#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
a=pd.Series([1,2,3,4,5,6,7])
print(a)


# In[8]:


import numpy as np
a1=pd.Series([1,2,3,4,5,(np.nan)])
print(a1)


# In[18]:


dates = pd.date_range('20190601',periods=20)
print(dates)


# In[17]:


lst=pd.date_range('20190601',periods=5)
print(lst)


# In[33]:


a3=pd.dataframe({'A':1,
                 'B':pd.Timestamp('20190601'),
                 'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                 'D':np.array([3]*4,dtype='int32'),
                 'E':pd.Categorial(["test","train","test","train"]),
                 'F':'foo'})
                 
                 
print(a3)


# In[ ]:


abcedefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz

