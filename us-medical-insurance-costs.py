#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# In[5]:


import pandas as pd
data = pd.read_csv('C:/Users/Asus/Downloads/python-portfolio-project-starter-files/python-portfolio-project-starter-files/insurance.csv')
data.head()


# In[8]:


data.describe()


# In[11]:


data.count()


# Find the average age of the patients

# In[12]:


data['age'].mean()


# Find the majority of the individuals are from

# In[14]:


data['region'].value_counts()


# Look at the different costs between smokers vs. non-smoker

# In[15]:


data['smoker'].value_counts()


# In[41]:


get_ipython().system('pip install plotly matplotlib seaborn --quiet')


# In[42]:


import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[43]:


sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (10, 6)
matplotlib.rcParams['figure.facecolor'] = '#00000000'


# In[46]:


fig = px.histogram(data, 
                   x='age', 
                   marginal='box', 
                   nbins=47, 
                   title='Distribution of Age')
fig.update_layout(bargap=0.1)
fig.show(renderer='iframe')


# In[49]:


fig = px.histogram(data, 
                   x='bmi', 
                   marginal='box', 
                   color_discrete_sequence=['red'], 
                   title='Distribution of BMI (Body Mass Index)')
fig.update_layout(bargap=0.1)
fig.show(renderer='iframe')


# In[ ]:


fig = px.histogram(data, 
                   x='charges', 
                   marginal='box', 
                   color='smoker', 
                   color_discrete_sequence=['red', 'grey'], 
                   title='Annual Medical Charges')
fig.update_layout(bargap=0.1)
fig.show(renderer='iframe')


# # Visualization of the distribution of medical charges in connection with other factors like "sex" and "region".

# In[51]:


fig = px.histogram(data,
                   x = 'charges',
                   color = 'sex',
                   color_discrete_sequence = ["blue","red"],
                   title = 'Different charges over genders'
               
)
fig.update_layout(bargap=0.1)
fig.show(renderer='iframe')


# In[52]:


fig = px.histogram(data,
                  x = "charges",
                  marginal = 'box', 
                   color="region",
                  title = "charges over different regions of U.S.A")
fig.update_layout(bargap=0.1)
fig.show(renderer='iframe')


# In[47]:


fig = px.histogram(data, x='smoker', color='sex', title='Smoker')
fig.show(renderer='iframe')


# In[48]:


fig = px.scatter(data, 
                 x='bmi', 
                 y='charges', 
                 color='smoker', 
                 opacity=0.8, 
                 hover_data=['sex'], 
                 title='BMI vs. Charges')
fig.update_traces(marker_size=5)
fig.show(renderer='iframe')


# In[53]:


fig = px.scatter(data, 
                 x='age', 
                 y='charges', 
                 color='smoker', 
                 opacity=0.8, 
                 hover_data=['sex'], 
                 title='Age vs. Charges')
fig.update_traces(marker_size=5)
fig.show(renderer='iframe')


# In[57]:


get_ipython().system('pip install nbconvert')
get_ipython().system('pip install pyppeteer')

