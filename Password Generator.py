#!/usr/bin/env python
# coding: utf-8

# To write a Python program to create a password, declare a string of numbers + uppercase + lowercase + special characters. Take a random sample of the string of a length given by the user:

# In[1]:


import random
password = int(input("Enter the length of password:"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,password ))
print(p)


# In[ ]:




