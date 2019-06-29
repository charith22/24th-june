#!/usr/bin/env python
# coding: utf-8

# In[1]:


s='charith22'
print(s.lower())


# In[2]:


s1="CHARITH22"
print(s1.islower())


# In[5]:


s2="a"
print(s2.upper())


# In[4]:


s2='A'
print(s2.isupper())


# In[10]:


s3='a1234'
s4='5678'
print(s4.isnumeric())
print(s3.isnumeric())


# In[11]:


s='charith'
s1='charith22'
print(s.isalpha())
print(s1.isalpha())


# In[12]:


s='charith22'
print(s.lower())
print(s.islower())
print(s.upper())
print(s.isupper())
print(s.isnumeric())
print(s.isalpha())


# In[13]:


s="Charith"
print(s.istitle())


# In[24]:


s1='charith '
s2='   '
print(s1.isspace())
print(s2.isspace())


# In[29]:


s1='charith'
print(" ".join(s1))
print("----".join(s1))


# In[30]:


print("---".join(["charith","charith"]))


# In[36]:


s1='c---h---a---r---i---t---h'
print(s1.split('---'))


# In[38]:


s1='charith 22'
print(s1.replace('charith','Charith'))


# In[39]:


s1='charith 22 22 22 22'
print(s1.replace('22','twenty two',2))


# In[46]:


s1='charith 22'
l=list(s1)
print(l)


# In[53]:


s=("charith",22,44,55,66,33)
print(s[0])
print(s[1])
print(s[1:4])
print(s[-1])
print(s[1:-3])


# In[54]:


s=("charith",22,44,55,66,33)
s1=(1,2,3,4,5,6,7,8)
s2=s+s1
print(s2)


# In[56]:


t1=("charith",22,44,55,66,33)
print(t1)
del(t1)
print(t1)


# In[68]:


u1={'name':'charith','age': 18,'phno':7032441420,'emailID':'charithblue22@gmail.com'}
print(u1["name"])
print(u1["emailID"])
print(u1["phno"])
print(u1['age'])


# In[83]:


u1={'name':'charith','age': 18,'phno':7032441420,'emailID':'charithblue22@gmail.com'}
print(u1['name'])
u1['name']='charith vyayavaram'
print(u1['name'])
u1['mob']='oct'
print(u1['mob'])
print(u1)
print(len(u1))


# In[81]:


u1={'name':'charith','age': 18,'phno':7032441420,'emailID':'charithblue22@gmail.com'}
del u1['age']
u1.clear()
del u1


# In[84]:


u1={'name':'charith','age': 18,'phno':7032441420,'emailID':'charithblue22@gmail.com'}
u2=u1.copy()
print(u1)
print(u2)


# In[89]:


u1={'name':'charith','age': 18,'phno':7032441420,'emailID':'charithblue22@gmail.com'}
print(u1.values())
u2=u1.copy()
print(u2.keys())
print(u1.items())


# In[95]:


l=['python','charith']
print("%s     %s"%(l[0],l[1]))


# In[99]:


l=['python','charith']
print("{0}     {1}".format(l[0],l[1]))


# In[10]:


contact={}
def addc(name,phn):
    if name not in contact:
        contact[name]=phn
        print("contact %s added" % name)
    else:
        print("already exist"% name)
    return
addc('charith',7032441420)
print(contact)
    
    
    
    
    


# In[14]:


def sc(name):
    if name in contact:
        print(contact[name])
    else:
        print("%s does not exists"% name)
    return

sc('rohan')
sc("charith")
    
    


# In[18]:


def newc(newcontacts):
    contact.update(newcontacts)
    print(len(newcontacts.keys()),"contacts added")
    return
newcontacts={"charith":34345343434,"rohan":4343434343}
newc(newcontacts)
print(contact)


# In[28]:


def delc(name):
    if name in contact:
        del contact[name]
        print(name,"deleted")
    else:
        print(name,"doesnt exist")
    return
delc("rohan")


# In[31]:


def mod(name,phn):
    if name in contact:
        contact[name]=phn
        print(name,"updated")
    else:
        print(name,"doesnt exist")
    return
mod("charith",70324414200)
print(contact)


# In[ ]:




