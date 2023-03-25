#!/usr/bin/env python
# coding: utf-8

# In[1]:


#string is a sequence of characters,and it ts basically collection of characters.
str1="kajol"
print(str1)


# In[2]:


str1="""kajol
rahul pokale"""
print(str1)


# In[6]:


text="python"
print(text[0])
print(text[1])
print(text[2])


# In[10]:


text="python"
print(text[-1])
print(text[-4])
print(text[-2])


# In[4]:


text="python"
print(text[1:4])
print(text[:4])
print(text[4:])
print(text[-1:])
print(text[:-1])


# In[1]:


str1="hello"
print(str1)


# In[5]:


s="hello"
print(s[1:4])


# In[16]:


s="python"
s[1:6:2]
s[:6:1]


# In[11]:


s="abcdefghij"
s[::2]
s[1:4:1]


# In[20]:


s="python"
s[len(s)-1]


# In[22]:


c=0
name=input("Enter name")
for i in name:
    if i in "aeiou":
        c+=1
print("no of vowels",c)


# In[23]:


c=0
name=input("Enter name")
for i in name:
    if i in "aeiou":
        c+=1
print("no of vowels",c)


# In[25]:


s="python"
print("o" not in "python")


# In[26]:


print("l" not in "kajol")


# In[39]:


str1="My name is kajol i am working with think quotient"
str1.replace("kajol","kaj") 
str1.replace(" & "," & ")


# In[31]:


s="kajol"
len(s)


# In[33]:


"   welcome to home".lstrip()


# In[34]:


"welcome to home     ".rstrip()


# In[35]:


"  kajol     ".strip()


# In[37]:


s="rahul"
s.capitalize()


# In[42]:


str1="KAJOL"
str1.lower()
str1.upper()


# In[46]:


s="rahul tanu"
s.title()


# In[47]:


str1="kajol"
str2="rahul"
str1.join(str2)


# In[51]:


s="Devang sareen!Tse!DaDS"
s.replace("sareen","sareen")


# In[ ]:


#str1=input()
#str1 is no or not?
#"-"
#str1=134243
str1=input("Enter string")



# In[54]:


s="hi red apple red bal red rose"
s.find('red')
idx.find("blue")


# In[ ]:


s="rahul"
s.swapcase()

