#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install opencv-python


# In[1]:


pip install plyer


# In[1]:


pip install plyer


# In[ ]:


import time 
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(title = "ALERT!!!",
            message = "Take a break! It has been an hour!",
            timeout = 10)
        time.sleep(3600)
        


# In[ ]:




