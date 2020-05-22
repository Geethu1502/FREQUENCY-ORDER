#!/usr/bin/env python
# coding: utf-8

# In[7]:


def main():
    input_string=input("please enter a string:")
    print(input_string)
main(input_string)
frequencies = {} 
  
for char in input_string: 
   if char in frequencies: 
      frequencies[char] += 1
   else: 
      frequencies[char] = 1

print ("Per char frequency in '{}' is :\n {}".format(input_string, str(frequencies)))


# In[ ]:





# In[ ]:




