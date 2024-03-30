#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sympy as sym


# In[2]:


# Define the symbol
x = sym.symbols('x')
# Define an expression
expression = 2*x - 1


# In[3]:


expression


# In[4]:


# Substitute 5 for x
expression.subs(x, 5)


# In[ ]:





# In[6]:


x,y = sym.symbols('x,y')


# In[7]:


x * y + y * x


# In[8]:


(x+y)**2


# In[9]:


g = (x+y)**2


# In[10]:


g.expand()


# In[11]:


x**2 - y**2


# In[12]:


(x**2 - y**2).factor()


# In[13]:


f = 8*x**4 - 4*x**3 + 10*x**2


# In[14]:


f


# In[15]:


f.subs(x, 3)


# In[16]:


f.factor()


# In[17]:


g = f / (2*x**2)


# In[18]:


g


# In[19]:


g.simplify()


# In[20]:


g.subs(x,0)


# In[21]:


g.simplify().subs(x,0)


# In[ ]:





# In[ ]:





# In[22]:


x,a,b,c = sym.symbols('x,a,b,c')


# In[23]:


fun = a*x**2 + b*x**3 + c*sym.exp(2*x)


# In[24]:


fun


# In[26]:


sym.diff(fun, x)


# In[27]:


fun.args


# In[28]:


for piece in fun.args:
    print(sym.diff(piece,x))


# In[ ]:





# In[29]:


x = sym.symbols('x')
fx = (5/4)*x + 9/4


# In[30]:


sym.plot(fx)


# In[31]:


sym.plot(fx, (x,-1,6), axis_center=[0,0])


# In[32]:


dydx = sym.diff(fx, x)


# In[33]:


print(f'The derivative of f(x) is {dydx}')


# In[ ]:





# In[34]:


x = sym.symbols('x')
fx = x**2
sym.plot(fx)
sym.plot(fx, (x,-1,6))


# In[35]:


fPrime = sym.diff(fx,x)


# In[36]:


fPrime


# In[37]:


sym.plot(fPrime, (x,-1,6))


# In[38]:


somePoints = [ -1, 0 ,2]


# In[40]:


for p in somePoints:
    print( f"f'({p}) = {fPrime.subs(x,p)}" )
    


# In[ ]:





# In[ ]:





# In[41]:


speed,time=sym.symbols('speed,time')


# In[42]:


distance = speed*time 


# In[43]:


ft = distance.subs( speed, 4 )


# In[44]:


dydx = sym.diff(ft, (time))


# In[46]:


dydx


# In[49]:


area_under_curve = sym.integrate(dydx , (time,0,3)  )


# In[50]:


area_under_curve


# In[51]:


sym.plot(dydx, (time,0,5) , axis_center=[0,0])


# In[ ]:





# In[ ]:





# In[ ]:





# In[52]:


# 25 m/s begins  = u
# accelerating at 3 m/s2 = a
# for 4 seconds = t


# In[53]:


# How far does the car travel in the 4 seconds it is accelerating?


# In[54]:


u,t,a = sym.symbols('u,t,a')


# In[55]:


s = u*t + 1/2*a*t**2


# In[56]:


s


# In[57]:


s = s.subs(a,3)


# In[58]:


s = s.subs(u,25)


# In[59]:


sym.plot(s)


# In[60]:


dsdt = sym.diff(s)


# In[61]:


dsdt


# In[62]:


total_distance_travelled = sym.integrate(dsdt, (t,0,4))


# In[63]:


total_distance_travelled


# In[64]:


acc = sym.diff(dsdt)


# In[65]:


sym.integrate(acc, (t))


# In[ ]:





# In[79]:


# find max storage of data in HD, where +48 in and -16 out


# In[66]:


t = sym.symbols('t')


# In[67]:


ft = 4 + 48*t - 16*t**2


# In[68]:


ft


# In[69]:


sym.diff(ft)


# In[71]:


dydt = sym.diff(ft)


# In[72]:


sym.plot(dydt)


# In[73]:


dydt


# In[74]:


# t = 1.5


# In[75]:


ft.subs(t,1.5)


# In[78]:


sym.plot(ft , 40 )


# In[ ]:




