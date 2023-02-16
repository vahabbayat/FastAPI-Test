#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fastapi import FastAPI


# In[2]:


app = FastAPI()


# In[3]:


@app.get('/')
def root():
    return ("This is path root for test the API")


# In[ ]:




