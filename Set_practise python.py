#!/usr/bin/env python
# coding: utf-8

# In[1]:


s1={1,2,3,4,4,3,4,2,4,3,4}
s1


# In[2]:


s1={"anjali",1,2,3,4,5,6,7,8,9,"vaibhav",94,10}
s1


# In[3]:


animals={"cat","dog","tiger","lion"}
print(animals)


# In[4]:


animals=set(["cat","dog","tiger","lion"])
print(animals)
animals.add("monkey")
print(animals)


# In[5]:


animals={"cat","dog","elephant","monkey"}
wild_animals={"lion","tiger","elephant",
animals.updat(wild_animals)
print(animals)


# In[ ]:


animals={"cat","dog","elephant","monkey"}
animals.discard("cat")#remove element
print(animals)
animals.remove("monkey")
print(animals)


# In[ ]:


animals={"cat","dog","elephant","monkey"}
animals.clear()
print(animals) #give empty set


# In[ ]:


even_numbers={2,4,6,8}
even_numbers
print(len(even_numbers))


# In[ ]:


#Q1
s1={1,2,3,4,4,3,4,2,4,3,4}
s1
s1.add(90)
s1


# In[ ]:


#Q3
set1={1,2,3,}
set2={'a','b','c'}
print(set1)
print(set2)
set3=set1.union(set2)
print(set3)


# In[ ]:


#Q2
s1={"dog","cat","elephant"}
s2={"lion","tiger","elephant"}
s3=s1.union(s2)
print(s3)


# In[ ]:


#Q4
s1={"dog","cat","elephant"}
s2={"lion","tiger","elephant"}
print(s1)
print(s2)
s3=s1.difference(s2)
print(s3)


# In[ ]:


count=2
while count<=5:
      print(count)
      count+=1


# In[ ]:


n=9
fact=1
while count<n+1:
    fact=fact*count
    count+=1
print(fact)


# In[ ]:


n=int(input("Enter the number:"))
a=n
sum=0
while n>0:
      r=n%10
      sum=sum+r**3
      n=n/10
if sum==a:
    print("armstrong number")
else:
    print(n="not armstromg number")


# In[ ]:


count=5
while count<=10:
       print(count)
       count+=1


# In[ ]:


count=1
number=int(input("Enter a number:"))
while count<=10:
      product=number*count
      print(product)
      count=count+1
      


# 

# In[ ]:


n=2
for i in range(1,11):
    print(n*i)


# In[ ]:


print("hello world")


# In[ ]:


x=7
print(x,'is a type',type(x))


# In[ ]:


a=10
b=20
if a<b:
    print("a is less than b")


# In[ ]:


a=int(input("Enter a value:"))
if a>0:
    print("a is positive")
elif a==0:
    print("a is zero")
else:
    print("a is negative")


# In[ ]:


a=55
if a%2==0:
    print("a is even")
else:
    print("a is odd")


# In[ ]:


a=3
b=7
if a>b:
    print("a is greater")
else:
    print("b is greater")


# In[ ]:


marks=int(input("Enter ur marks:"))
if marks>=35:
    print("congratulations u have passed")
    if marks>=90:
        print("Grade A")
    elif marks>=75:
        print("Grade B")
    elif marks>=60:
        print("Grade C")
    elif marks>=35:
        print("Grade D")
    else:
        print("Bad luck u failed")
        


# In[ ]:


for i in range(5):
    print(i)


# In[ ]:


for x in "banana":
    print(x)


# In[ ]:


lang=["java","c++","c","python"]
for language in lang:
    print(language)


# In[ ]:


for i in range(2,22,2):
    print(i)
    
    


# In[ ]:


for  i in range(1,11):
    if i==5:
        break
    print(i)


# In[ ]:


for i in range(1,11):
    if i==5:
        continue
    print(i)


# In[ ]:


for i in range(1,11):
    pass


# In[ ]:


num=int(input("Enter a number:"))
count=1
for count in range(1,11):
    product= num*count
    print(num,"x",count,"=",product)


# In[ ]:


num=int(input("Enter a number:"))
count=1
for count in range(1,11):
    product=num*count
    print(num,"x",count,"=",product)


# In[ ]:


for i in range(2,22,2):
    print(i)


# In[ ]:


i=1
n=5
while i<=n:
    print(i)
    i=i+1


# In[ ]:


i=1
while i<6:
    print(i)
    if(i)==3:
        break
    i=i+1


# In[ ]:


count=0
while count<3:
    print("kajol")
    count=count+1
else:
    print("kajol pokale")


# In[ ]:


i=1
while i<6:
    print(i)
    i=i+1
else:
    print("i is no longer less than 6.")


# In[ ]:


i=5
while i>=1:
     print(i)
     i=i-1


# In[ ]:


n=int(input("Enter a number:"))
a=n
sum=0
while n>0:
    r=n%10
    sum=sum+r**3
    n=n//10
if sum==a:
    print("armstrong number")
else:
    print("not armstrong number")


# In[23]:


list1=[15,13,5,20,16,14,16,17,18,14,9]
print(list1)
print(len(list1))
min(list1)
max(list1)
sum(list1)
list1.insert(1,"kaju")
print(list1)


del list1[1]
print(list1)
list1.sort()
print(list1)

sorted(list1,reverse=True)
print(count(list1))
print(list1)


# In[ ]:


list1=["kajol",3,4,True]
print(list1)

print(type(list1))


# In[ ]:


list1=(("kajol","pari","rahul"))
print(list1)


# In[16]:


list1=["pyhon","java","c++","c","cdotnet"]
print(list1)
print(list1[-1])
print(list1[2])
print(list1[1:3])
print(list1[:])
list1.append("sql")
print(list1)
list2=["sqlplus","postresql"]
list1.extend(list2)
print(list1)
list1[2]='clang'
print(list1)
del list1[2]
print(list1)
del list1[1:4]
print(list1)
list1.remove("sql")
print(list1)
"pyhon" in list1
list1.pop()
print(list1)
list1.pop(1)
print(list1)
list1=["pyhon","java","c++","c","cdotnet"]
print(list1)
print(list1.count("java"))


# In[24]:


my_tuple=("a","b","c","d")
print(my_tuple)


# In[6]:


my_tuple=()
print(my_tuple)
my_tuple=(1,2,3,4)
print(my_tuple)
my_tuple=(1,"kajol",True)
print(my_tuple)
my_tuple=("kajol",(8,4,6),(1,2,3))
print(my_tuple)
my_tuple=("kajol",)
print(my_tuple)
print(type(my_tuple))


# In[13]:


letters=("p","r","o","g","r","a","m","i","z")
print(letters)
print(letters[0])
print(letters[6])
print(letters[-1])
print(letters[1:4])
print(letters[:-7])


# In[21]:


my_tuple=("a","p","p","l","l","e")
print(my_tuple)
print(my_tuple.count("l"))
print(my_tuple.index("e"))
print()


# In[23]:


my_tuple=("python","java","swift")
for i in my_tuple:
    print(i)


# In[2]:


s1={1,2,3,4,5,1,2,3,4,5}
print(s1)


# In[4]:


str1="kajol"
str1
ord("k")


# In[4]:


s1={"apple","banana","cherry"}
for i in s1:
    print(i)
"banana" in s1


# In[1]:


s2={True,False,False}
s2
print(type(s2))


# In[8]:


empty_set={}
empty_set


# In[12]:


s2=set((1,2,3,4,5,6))
print(s2)
s2.add(9)
s2
s2.discard(3)
s2
s2.pop()
s2
print(len(s2))
s2


# In[15]:


s1={1,2,3,4,5}
s1
s2={5,6,7,8,9}
s3=s1.union(s2)
print(s3)
s3= s1 | s2


# In[20]:


s1={1,2,3,4,5}
s1
s2={1,2,6,7,8}
s2
s3=s1.intersection(s2)
s3
s3= s1 & s2
s3


# In[23]:


s1={1,2,3,4,5}
s1
s2={1,2,6,7,8}
s2
s3=s1.difference(s2)
s3
s=s1 - s2
s3


# In[24]:


capital_city={"Nepal":"kathmandu","Italy":"Rome","England":"London"}
print(capital_city)


# In[27]:


numbers={1:"one",2:"two",3:"three"}
print(numbers)


# In[28]:


dict_one={"brand":"Ford","model":"Mustang","year":1994,"year":2020}
print(dict_one)


# In[32]:


print(12+23)
print(12-2)
print(12*2)
print(12/3)
      


# In[37]:


a=12
print(a)
a+=2
print(a)


# In[38]:


a,b=10,12
print(a==b)


# In[43]:


a=True
b=False
print(a and b)
print(a or b)
print( not a)


# In[46]:


list1=["kajol","rahul","pavan"]
print("rahul" in list1)
cities=("pune","mumbai","delhi")
print("nagpur" not in cities)


# In[48]:


a=10
b=12
print(a is b)
print(a is not b)


# In[53]:


a=10
b=12
print(a & b)
print(a | b)
print(a ^ b)
print(~ b)
print(~ a)


# In[12]:


s1={1,2,3,4,5,6}
s2={7,1,8,9,5,3}
print(s1)
print(type(s1))
for i in s1:
    print(i)
s1.add(7)
print(s1)
s1.discard(4)
print(s1)
s3=s1.union(s2)
print(s3)
s3=s1.intersection(s2)
print(s3)
s3=s1.difference(s2)
print(s3)


# In[22]:


foprint(stu_id[1])
del stu_id[2]
print(stu_id)
for i in stu_id:
    print(i)


# In[1]:


for i in range(1,11):
    if i==4:
        break
    print(i)


# In[2]:


for i in range(1,11):
    if i==4:
        continue
    print(i)


# In[3]:


for i in range(1,11):
    pass


# 

# In[8]:


number = 10
site_name="programiz.com"
print(site_name)
site_name="apple.com"
print(site_name)
a,b,c=1,"kajol",3.5
print(a)
print(b)
print(c)
site1=site2="programiz.com"
print(site1)
print(site2)


# In[12]:


num1="kajol"
print(type(num1))
list1=[1,2,3]
print(list1)
print(type(list1))


# In[13]:


a=4
b=6
if a<b:
    print("a is less than b")


# In[16]:


x=55
if x%2!=0:
    print("x is even number")
else:
    print("x is odd number")


# In[19]:


a=200
b=33
c=500
if a>b and c>a:
    print("Both conditions are true")


# In[21]:


a=200
b=33
c=500
if a>b or a>c:
    print("at least one conditions is true")


# In[24]:


x=int(input("Enter a value:"))
if x>0:
    print("x is positive")
elif x==0:
    print("x is zero")
else:
    print("x is negative")


# In[28]:


marks=int(input("Enter a marks:"))
if marks>=35:
    print("congratulation u are passesd")
    if marks>=90:
        print("Grade A")
    elif marks>=75:
        print("Grade B")
    elif marks>=60:
        print("Grade C")
    elif marks>=35:
        print("Grade D")
    else:
        print("you are failed")


# In[32]:


for i in range(11):
    print(i)
    


# In[33]:


for x in "banana":
    print(x)


# In[34]:


i=1
n=5
while i<=n:
    print(i)
    i=i+1


# In[39]:


print(1+2)
print(2-1)
print(2*1)
print(3%9)


# In[43]:


a=10
b=12
print(a==b)
print(a>b)
print(a>=b)
print(a!=b)


# In[45]:


a=12
print(a)
a+=2
print(a)


# In[48]:


list1=[1,2,3,4]
print(list1)
print(5 in list1)
print(2 not in list1)


# In[50]:


a=10
b=12
print(a is b)
print(a is not b)


# In[55]:


a=10
b=12
print(a & b)
print(a | b)
print(a ^ b)
print( ~ b)
print(~a)


# In[ ]:




