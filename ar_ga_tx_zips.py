#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
texas_zips=pd.read_csv('./data/texas_zips.csv')


# In[2]:


texas_zips.info()


# In[3]:


texas_zips.shape


# In[4]:


texas_zips.describe()


# In[5]:


texas_zips.head()


# In[6]:


arkansas_zips=pd.read_csv('./data/arkansas_zips.csv')


# In[7]:


arkansas_zips.info()


# In[8]:


arkansas_zips.shape


# In[9]:


arkansas_zips.describe()


# In[10]:


arkansas_zips.head()


# In[11]:


georgia_zips=pd.read_csv('./data/georga_zips.csv')


# In[12]:


georgia_zips.info()


# In[13]:


georgia_zips.shape


# In[14]:


georgia_zips.describe()


# In[15]:


georgia_zips.head()


# In[16]:


ar_ga_tx = pd.concat([arkansas_zips, georgia_zips, texas_zips])


# In[17]:


ar_ga_tx.shape


# In[18]:


georgia_zips.shape


# In[19]:


texas_zips.shape


# In[20]:


arkansas_zips.shape


# In[21]:


state_counts=(arkansas_zips.shape[0]+georgia_zips.shape[0]+texas_zips.shape[0])
state_counts


# In[22]:


state_counts == ar_ga_tx.shape[0]


# In[23]:


all_zips_coords = pd.read_csv('./data/uszips.csv')


# In[24]:


all_zips_coords.head()


# In[25]:


all_zips_coords[['zip', 'latitude', 'longitude']]=all_zips_coords['ZIP,LAT,LNG'].str.split(',',3, expand=True)


# In[26]:


all_zips_coords.head()


# In[27]:


all_zips_coords= all_zips_coords.drop(columns=['ZIP,LAT,LNG'])


# In[28]:


all_zips_coords.head()


# In[29]:


all_zips_coords.info()


# In[30]:


all_zips_coords['zip']=all_zips_coords['zip'].astype(str).astype(int)


# In[31]:


all_zips_coords[['latitude', 'longitude']]=all_zips_coords[['latitude', 'longitude']].astype(str).astype(float)


# In[32]:


all_zips_coords.info()


# In[33]:


ar_ga_tx_combined_coo_zip=pd.merge(ar_ga_tx, all_zips_coords, how='left', on='zip')


# In[34]:


ar_ga_tx_combined_coo_zip.info()


# In[35]:


ar_ga_tx_combined_coo_zip.shape[0]==ar_ga_tx.shape[0]


# In[36]:


ar_ga_tx_combined_coo_zip


# In[37]:


ar_ga_tx_combined_coo_zip.info()


# In[38]:


ar_ga_tx_combined_coo_zip.to_csv('ar_ga_tx_combined_coo_zip.csv')

