#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy; 
import numpy as np;
a = np.array([1,2,3,4,5]);
b = np.array([9,10]);
print(a);
print(b);


# In[10]:


print ('the shape of a is:', a.shape)


# In[13]:


print("the shape of b is:",b.shape)


# In[17]:


x = np.array([[1,2], [3,4]]);
print(x);


# In[19]:


print("the shape of x is:", x.shape)


# In[20]:


w = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(w)


# In[22]:


print("the shape of w is:", w.shape)


# In[28]:


a10 = np.arange(10)
a10


# In[29]:


a10.shape


# In[ ]:





# In[16]:


import pandas as pd
data = {"Name": ["ayo", "ade", "akin"], "Age": [10, 15, 14]}
df = pd.DataFrame(data)
df


# In[17]:


#population and area (km/square) of some states in Nigeria and their capital;
dict_data = {"state": ["Abia", "Adamawa", "Lagos", "osun", "Rivers"],
             "Capital": ["Umuahia", "Yola", "Ikeja", "Osogbo", "Portharcourt"],
             "Area": [6320, 36917, 3345, 9251, 11077],
             "Population":[2845380, 3178950, 9113605, 3416959, 5198605]}
df = pd.DataFrame(dict_data)
df


# In[22]:


import numpy as np
import pandas as pd
df = pd.read_excel('dsn.xlsx')
df

