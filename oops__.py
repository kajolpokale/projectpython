#!/usr/bin/env python
# coding: utf-8

# In[1]:


class student:
    name=""
    age=0
student1=student()
student1.name="kajol"
student1.age=16
student2=student()
student2.name="rahul"
student2.age=15
print(student1.name,student1.age)


# In[2]:


class car:  
    def __init__(self,modelname, year):  
        self.modelname = modelname  
        self.year = year  
    def display(self):  
        print(self.modelname,self.year)  
  
c1 = car("Toyota", 2016)  
c1.display()  


# In[3]:


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        def get.age(self):
            return self.age


# In[ ]:


class student:
    def __init__(self):
        pass

def main():
    student = student()
    print("student object oriented.")

if __name__ == "__main__":
    main()


# In[ ]:


classs student:
    school_name = "saraswati vidya mandir"
    
    def __init__(self,name,age,):
        self.name = name
        self.age = age
        
   
 def main():
        student1=student("Ram",17)
        student2=student("shayam",15)
        print(student1.age,student1.name)


# In[ ]:


#multilevael inheritance
class vehicle:
    def __init__(self.num_of_wheels,engine_power,vehicle_type):
        self.num_of_wheels=num_of_wheels
        self.engine_power=engine_power
        self.vehicle_type=vehicle_type
        
    def print_vehicle_attributes(self)
    


# In[ ]:


#inheristance method overriding
class shape:
    def __init__(self,sides):
        self_sides=sides
    
    def print_shape(self):
        print("This shape is no defined")
        
    def print_sides(shape):
        print(self.sides)
        
class square(shape):
    def __init__(self,sides):
        super().__init__(sides)
    
    def print_shape(self):
        print("This shape is square")
        
class circle(square):
    def __init__(self,sides):
        self.sides=sides
        
    def print_shape(self):
        print("This shape is circle.")
        
class Triangle(circle):
    def __init__(self,sides):
        pass

def main():
    circle=circle(108)
    square=square(4)
    square.print_shape()
    square.print-sides()
    triangle=triangle(3)
    triangle.print_shape()
    
if __name__ == "__main__":
   main()
    


# In[ ]:


#inheritance method overriding __LSP__
class square(shape):
    def __init__(self,sides):
        


# In[4]:


#Q1 assignment
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Teacher(Person):
    
    def isTeacher(self):
         return f"{self.name} is a Teacher"
        
mam = Teacher("kajol", 30)

print(mam.isTeacher())


# In[ ]:


#Q2 assign
class Parent:
    str1 = "kajol"
    
class Child(Parent):
    str2 = "rahul"
    
class GrandChild(Child):
    
    def get_str(self):
        print(self.str1 + self.str2)
        
person = GrandChild()
person.get_str()


# In[ ]:


#Q3 assign
class SuperClass:
    x = 3
    
class SubClass1(SuperClass):
    pass

class SubClass2(SuperClass):
    pass

class SubClass3(SuperClass):
    pass

a = SubClass1()
b = SubClass2()
c = SubClass3()
print(a.x, b.x, c.x)


# In[ ]:


class Girl:
    name = "kajolpokale"
 
 
if __name__ == '__main__':
    Girl = Girl()
    print("Before deleting name attribute from kajol object:")
    print(kajol.name)
    delattr(kajol, "name")
    print("After deleting name attribute from kajol object:")
    # this will raise AttributeError if we try to access 'domain' attribute
    print(kajol.name)


# In[2]:


#inheristance lsp.py
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.length=breadth
        
    def set.length(self,length):
        self.length=length
        
    def set.breadth(self,breadth):
        self.breadth=breadth
        
class square(Rectangle):
    self __init__(self,length):
        super() __init__length,length)
        
    def set_length(self,length):
        self>length=self.breadth=length
        
    def set_breadth(self,breadth):
        self.length=self.breadth=breadth
        
def calculate-area(obj):
    obj.set_length(10)
    if obj.length*obj.breadth==10*obj.breadth:
        return "Area is" +str(10*obj.breadth)
    
def main():
    rect=Rectangle(4,5)
    square=square(4)
    print(calculate_area(rect))
    print(calculate_area(square))
    
if __name__ == "__main__":
    main()
    


# In[ ]:




