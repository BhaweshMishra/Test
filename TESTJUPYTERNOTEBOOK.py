#!/usr/bin/env python
# coding: utf-8

# In[75]:


import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import datetime
import seaborn as sns


# In[76]:


a=np.array([1,2,3,4,5])
print(a)


# In[77]:


asu=pd.DataFrame({'A':pd.Series([1,3,5,7,3],index=a[0:5]),
                  'B':[8,2,3,4,5],
                  'C':[1,2,3,4,5]
                 },index=a)
asu


# In[78]:


pd.Series([1,2,3,4,5],index=[1,2,3,4,5]).shift(2)


# In[79]:


c=asu.columns
i=asu.index
v=np.array(asu)
p=np.transpose(v)
df=pd.DataFrame(p,index=c,columns=i)
print(df)


# In[80]:


t=asu.loc[0:3,'B':'C']
print(t)
print('----------')
j=asu.iloc[0:3,1:3]
print(j)


# In[81]:


asu.at[3,'B']=9
asu


# In[82]:


df=asu.reindex(index=[1,2,3,4,5,6,7],columns=['A','B','C','D','E'])
df['D'][5]=7
x=df.isnull()
df


# In[83]:


df=df.fillna(value=4)
df


# In[84]:


x=df.mean(1)
asu['A']


# In[85]:


asu[0:1]


# In[86]:


j=pd.Series(['hello','my','name','is'])


# In[87]:


j.str.upper()


# In[88]:


left=pd.DataFrame({'A':[1,2,3,4],
                'B':[2,3,4,5],})
print(left)
right=pd.DataFrame({'A':[5,2,3,7],
                   'C':[10,11,12,13]})
right


# In[89]:


pd.merge(left,right,on='A')


# In[90]:


asu.groupby('A').sum()


# In[91]:


tupp=list(zip(*[(1,2,3,4),(11,22,33,44)]))
tupp
l=[[1,2],[1,4],[5,6]]
l
index=pd.MultiIndex.from_tuples(l,names=['First','Second'])
index


# In[92]:


df=pd.DataFrame(np.random.randn(3,2),index=index,columns=['A','B'])
print(df)
print(df.stack())


# In[93]:


df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
                         "bar", "bar", "bar", "bar"],
                   "B": ["one", "one", "one", "two", "two",
                         "one", "one", "two", "two"],
                   "C": ["small", "large", "large", "small",
                         "small", "large", "small", "small",
                         "large"],
                   "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})
df
table = pd.pivot_table(df, values=['D'], index=['A','B'],
                    columns=['C'])
table


# In[94]:


ts=pd.Series(np.random.randn(100))
ts
tf=ts.cumsum()
tf.plot()
ts.plot()


# In[95]:


x=pd.read_csv(r'C:\Users\Pankaj M\financial_data.csv')
list(x.columns[1:])
m=pd.DataFrame(np.array(x.iloc[0:,1:]),index=x['Date'],columns=list(x.columns[1:]))
m
m.plot()


# In[96]:


w=0.25
c=[1,2,3,4,5,6]
c1=[1+w,2+w,3+w,4+w,5+w,6+w]
d=np.random.randint(1,6,size=6)
e=np.random.randint(1,6,size=6)
f=np.random.randint(1,6,size=6)
print(d)
print(e)
print(f)


# In[97]:


plt.bar(c,d,width=0.25)
plt.bar(c1,e,color='green',width=0.25)
plt.xticks(np.arange((1.25+1)/2,7,1))
plt.show()


# In[98]:


a = np.array([22, 87, 5, 43, 56,  
              73, 55, 54, 11, 
              20, 51, 5, 79, 31, 
              27]) 
  
# Creating histogram 

plt.hist(a, bins = [0, 25, 50, 75, 100],width=5) 
plt.xticks(np.arange(0,100,25))
# Show plot 
plt.show()


# In[99]:


a=sns.load_dataset('flights')
sns.relplot(x='passengers',y='month',data=a)


# In[104]:


a=sns.load_dataset('flights')
sns.relplot(x='passengers',y='month',hue='year',data=a)


# In[142]:


b=sns.load_dataset('tips')
sns.relplot(x='day',y='total_bill',data=b,)
sns.catplot(x='day',y='total_bill',data=b,kind='boxen')


# In[156]:


import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('iris')
sb.distplot(df['petal_length'],kde=True,hist=True)
plt.show()


# In[153]:


import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('iris')
sb.distplot(df['petal_length'])
plt.show()


# In[159]:


import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('titanic')
sb.barplot(x = "sex", y = "survived", hue = "class", data = df)
plt.show()


# In[ ]:




