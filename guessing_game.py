#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random 
number = random.randint(1,100)
attempts = 0
print("Number Guessing Game ")
print("I have picked a number between 1 and 100 ")
while True :
    guess = int(input("Your guess :"))
    attempts +=1
    if guess < number:
        print("Too low, try again")
    elif guess > number:
        print("Too high, try again")
    else:
        print("Correct! Attempts:",attempts)
        break


# In[ ]:




