#!/usr/bin/env python
# coding: utf-8

# ### SENSUS API for zipcode: https://api.census.gov/data/2020/acs/acs5?get=NAME,group(B19013)&for=zip%20code%20tabulation%20area:*
# 
# ### how to zip: https://www2.census.gov/data/api-documentation/how-to-download-all-zip-code-tabulation-areas-from-the-census-api.pdf
# 
# ### https://api.census.gov/data/2020/
# 
# ### https://www.census.gov/data/developers/data-sets/popest-popproj/popest.html
# 
# ### how to get pop data with census api: https://api.census.gov/data/2021/pep/population?get=DENSITY_2021,POP_2021,NAME,STATE&for=region:*&key=YOUR_KEY
# 
# ### https://www.census.gov/geographies/reference-files/time-series/geo/gazetteer-files.2021.html#list-tab-6MPRXXDBDK2UUWTSHX
# 
# ### https://data.census.gov/table?g=0400000US48
# 
# ### https://gist.githubusercontent.com/erichurst/7882666/raw/5bdc46db47d9515269ab12ed6fb2850377fd869e/US%2520Zip%2520Codes%2520from%25202013%2520Government%2520Data
# 

# In[1]:


import pandas as pd
texas_zips=pd.read_csv('./texas_zips.csv')


# In[2]:


texas_zips.info()


# In[3]:


texas_zips.shape


# In[4]:


texas_zips.describe()


# In[5]:


texas_zips.head()


# In[6]:


arkansas_zips=pd.read_csv('./arkansas_zips.csv')


# In[7]:


arkansas_zips.info()


# In[8]:


arkansas_zips.shape


# In[9]:


arkansas_zips.describe()


# In[10]:


arkansas_zips.head()


# In[11]:


georgia_zips=pd.read_csv('./georga_zips.csv')


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


all_zips_coords = pd.read_csv('./uszips.csv')


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

