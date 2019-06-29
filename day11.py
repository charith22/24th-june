#!/usr/bin/env python
# coding: utf-8

# In[4]:


def t():
    print("t() for function")
    return
t()


# In[2]:


class a:
    def t(s):
        print("t() for class and method")
        return
obj=a()
obj.t()


# In[8]:


class a1:
    def f(s,n):
        fact=1
        while(n!=0):
            fact=fact*n
            n=n-1
        return fact
o=a1()
o.f(22)


# In[10]:


class d:
    def __init__(s,p1,p2):
        s.p1=p1
        s.p2=p2
    def add(s,p1,p2):
        return p1+p2
c1=d(10,20)
print(c1.add(222,222))

        
    


# In[23]:


class person(object):
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self.name
    def isemployee(self):
        return False
class employee(person):
    def isemployee(person):
        return True
    
emp=person("charith")
print(emp.getname(),emp.isemployee())

emp=employee("rohan")
print(emp.getname(),emp.isemployee())


# In[26]:


l=[1,2,3,4,5,6,7,8,9]
print(l)


# In[28]:


import numpy as np
l=[1,2,3,4,5,6,7,8,9]
array=np.array(l)
print(array)


# In[29]:


l=[1,2,3,4,5,6,7,8,9]
array=np.array(l)
print(array.shape)
print(array.dtype)


# In[30]:


l=[1.2,2.2,3.2]
array=np.array(l)
print(array.shape)
print(array.dtype)


# In[32]:


a1=np.array([(1,2,3),(4,5,6)])
print(a1.shape)
a2=np.array([(1,2),(3,4),(4,5)])
print(a2.shape)


# In[52]:


a1=np.array([(1,2,3),(4,5,6),(7,8,9),(10,11,12)])
print(a1)
a1.reshape(12,1)


# In[72]:


a1=np.array([(1,2,3)])
a2=np.array([(4,5,6)]) 
a3=np.array([(7,8,9)])
print(np.hstack((a1,a2)))
print(np.vstack((a1,a2)))


# In[58]:


np.zeros((2,2),dtype=np.int64)


# In[60]:


np.ones((4,3),dtype=np.int64)


# In[70]:


a=np.matrix(np.ones((4,4),dtype=np.int64))
np.asarray(a)[2][3]=5
print(a)


# In[71]:


a=np.matrix(np.ones((4,4),dtype=np.int64))
np.array(a)[2]=5
print(a)


# In[80]:


a=np.matrix(np.ones((3,3),dtype=np.int64))
np.asarray(a)[1][1]=5
print(a)
print(np.asarray(a)[0][0]+np.asarray(a)[1][1]+np.asarray(a)[2][2])


# In[82]:


import numpy as np
np.arange(1,10)


# In[83]:


np.arange(1,100,9)


# In[84]:


np.arange(22,222,2)


# In[103]:


a1=np.array([(1,2,3),(4,5,6)])
print(a1[:,1])
print(a1[0])
print(a1[1])
print(a1[:,2])
print(a1[1:,1])


# In[104]:


a2=np.random.normal(5,1,10)
print(a2)
print("min",np.min(a2))
print("max",np.max(a2))
print("mean",np.mean(a2))
print("median",np.median(a2))


# In[113]:


c1=np.array([(1,2,3),(2,2,2),(1,3,5)])
c2=np.array([(4,5,6),(1,2,3),(2,2,2)])
np.dot(c1,c2)


# In[114]:


c1=np.array([(1,2,3),(2,2,2),(1,3,5)])
c2=np.array([(4,5,6),(1,2,3),(2,2,2)])
np.cross(c1,c2)


# In[115]:


c1=np.array([(1,2,3),(2,2,2),(1,3,5)])
c2=np.array([(4,5,6),(1,2,3),(2,2,2)])
np.matmul(c1,c2)

