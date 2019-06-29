#!/usr/bin/env python
# coding: utf-8

# In[58]:


def cf(fn):
    f=open(fn,"w")
    for i in range(10):
        f.write(" %d Steps \n"%i)
    print("file created!!!")    
    f.close()    
    return
cf('charith')
cf('rohan')
cf('chinmay')


# In[59]:


def rf(fn):
    f=open(fn,"r")
    if (f.mode=='r'):
        x=f.read()
        print(x)
    f.close()
    return
rf('charith')


# In[60]:


def ad(fn):
    f=open(fn,"a")
    f.write("new line\n")
    f.write("new line")
    print("data is appended")
    return
ad("charith")
rf("charith")


# In[62]:


def da(fn,word):
    f=open(fn,'r')
    if f.mode=='r':
        x=f.read()
        lst=x.split()
    cnt=lst.count(word)    
    return cnt
print(da('charith','a'))
print(da('charith','Steps'))
    


# In[63]:


def cc(fn):
    f=open(fn,'r')
    if f.mode=='r':
        x=f.read()
        lst=list(x)
    return len(lst)
print(cc('charith'))
    


# In[64]:


def cou(filename): 
    countupper=0
    f=open(filename)
    if (f.mode=='r'):
        x=f.read()
        lst=list(x)
    for i in lst:
        if i.isupper():
            countupper+=1
    return countupper
print(cou('charith'))


# In[66]:


def col(filename): 
    countlower=0
    f=open(filename)
    if (f.mode=='r'):
        x=f.read()
        lst=list(x)
    for i in lst:
        if i.islower():
            countlower+=1
    return countlower
print(col('charith'))


# In[67]:


def cow(filename): 
    countspace=0
    f=open(filename)
    if (f.mode=='r'):
        x=f.read()
        lst=list(x)
    for i in lst:
        if i.isspace():
            countspace+=1
    return countspace
print(cow('charith'))


# In[70]:


def cc(fn):
    f=open(fn,'r')
    if f.mode=='r':
        x=f.read()
        lst=x.split('\n')
    return len(lst)
print(cc('charith'))
    


# In[88]:


import re
def pnv(phn):
    p='^[6-9][0-9]{9}$'
    phn=str(phn)
    if re.match(p,phn):
        return True
    else:
        return False
print(pnv(97032441420))
print(pnv(7032441420))
print(pnv(9963900396))


# In[93]:


import re
def pnvr(phn):
    p='^[0][4][0][-][6-9][0-9]{9}$'
    phn=str(phn)
    if re.match(p,phn):
        return True
    else:
        return False
print(pnvr('040-7032441420'))    


# In[92]:


import re
def pnvr1(phn):
    p='^[+][9][1][6-9][0-9]{9}$'
    phn=str(phn)
    if re.match(p,phn):
        return True
    else:
        return False
print(pnvr1('+917032441420'))    


# In[103]:


import re
def r1(r):
    p='^[2][2][1][8][1][0][3][0][4][0][1-9]{1}[1-9]{1}$'
    r=str(r)
    if re.match(p,r):
        return True
    else:
        return False
print(r1('221810304062'))    
print(r1('22181030402'))    


# In[ ]:





# In[109]:


import re
def n1(n):
    p='^[T][S][A-Z|0-9]{2}[A-Z|0-9]{2}[0-9]{4}$'
    n=str(n)
    if re.match(p,n):
        return True
    else:
        return False
print(n1('TSAB128188'))  
print(n1('TSAB122222'))  


# In[108]:


import re
def em(i):
    p='^[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][a-z0-9]{3,18}[.][a-z]{2,4}$'
    if re.match(p,i):
        return True
    else:
        return False
print(em('charithblue22@gmail.com'))    


# In[ ]:




