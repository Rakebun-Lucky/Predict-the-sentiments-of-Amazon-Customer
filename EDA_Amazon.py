#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

df = pd.read_csv('E:\Projects\Amazon use-case\Reviews.csv')


# In[2]:


df.head()


# In[4]:


df.columns


# In[7]:


df['Helpful%'] = np.where(df['HelpfulnessDenominator']>0,df['HelpfulnessNumerator']/df['HelpfulnessDenominator'],-1)


# In[8]:


df.head()


# In[9]:


df['Helpful%'].unique()


# In[11]:


df['%upvote'] = pd.cut(df['Helpful%'],bins=[-1,0,0.2,0.4,0.6,0.8,1],labels=['Empty','0-20%','20-40%','40-60%','60-80%','80-100%'])


# In[12]:


df.head()


# In[13]:


df.groupby(['Score','%upvote']).agg('count')


# In[16]:


df_s = df.groupby(['Score','%upvote']).agg({'Id':'count'}).reset_index()


# In[17]:


df_s


# In[19]:


pivot = df_s.pivot(index='%upvote',columns='Score')


# In[20]:


pivot


# In[42]:


import seaborn as sns

sns.heatmap(pivot,annot=True,cmap='YlGnBu')


# In[ ]:




