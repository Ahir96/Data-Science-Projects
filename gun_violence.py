#!/usr/bin/env python
# coding: utf-8

# # Gun Violence Project

# For this project we will be analyzing some gun violence data from Kaggle. The data contains the following fields:
# 
# incident_id
# 
# dateDate of crime
# 
# stateState of crime
# 
# city_or_countyCity/ County of crime
# 
# addressAddress of the location of the crime
# 
# n_killedNumber of people killed
# 
# n_injuredNumber of people injured
# 
# incident_urlURL regarding the incident
# 
# source_urlReference to the reporting source
# 
# incident_url_fields_missingTRUE if the incident_url is present, FALSE otherwise
# 
# congressional_districtCongressional district id
# 
# gun_stolenStatus of guns involved in the crime (i.e. Unknown, Stolen, etc...)
# 
# gun_typeTypification of guns used in the crime
# 
# incident_characteristicsCharacteristics of the incidence
# 
# latitudeLocation of the incident
# 
# location_description
# 
# longitudeLocation of the incident
# 
# n_guns_involvedNumber of guns involved in incident
# 
# notesAdditional information of the crime
# 
# participant_ageAge of participant(s) at the time of crime
# 
# participant_age_groupAge group of participant(s) at the time crime
# 
# participant_genderGender of participant(s)
# 
# participant_nameName of participant(s) involved in crime
# 
# participant_relationshipRelationship of participant to other participant(s)
# 
# participant_statusExtent of harm done to the participant
# 
# participant_typeType of participant
# 
# sourcesParticipants source
# 
# state_house_districtVoting house district
# 
# state_senate_districtTerritorial district from which a senator to a state legislature is elected.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv("gun-violence-data_01-2013_03-2018.csv")


# In[3]:


df.info()


# ** Check the head of the df **

# In[47]:


df.head(3)


# What are the top 10 states for gun violence from the csv file?

# In[7]:


df['state'].value_counts().head(10)


# What is the maximum number of injury from the gun violence?

# In[30]:


df['n_injured'].value_counts().max()


# What is the kill count of the state Colorado?

# In[45]:


df[df['state']=='Colorado']['n_killed'].count()


# What is the age of a participant named 'Bernard Gillis'?

# In[46]:


df[df['participant_name']=='0::Bernard Gillis']['participant_age']


# How many of the participants were involved in Chicago?

# In[87]:


df[df["city_or_county"] == 'Chicago']['participant_name'].count()


# In which year the highest amount of gun violence took place?

# In[93]:


df['Year'] = df['date'].apply(lambda date: date.split('-')[0])


# In[127]:


df['Year'].value_counts().head(1)


# Create a counterplot using seaborn from the years of gun violence

# In[99]:


sns.countplot(x='Year',data=df,palette='cubehelix')


# In[131]:


df['date'] = pd.to_datetime(df['date'])


# In[138]:


df['Month'] = df['date'].apply(lambda date: date.month)
df['Dayofweek'] = df['date'].apply(lambda date: date.dayofweek)
df['Year'] = df['date'].apply(lambda date: date.year)


# In[139]:


dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}


# In[140]:


df['Dayofweek'] = df['Dayofweek'].map(dmap)


# In[150]:


sns.countplot(x='Dayofweek',data=df,hue='Year',palette='viridis')

# To relocate the legend
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)


#  Now use seaborn to create a countplot of the months with the hue based off of the Year column

# In[152]:


sns.countplot(x='Month',data=df,hue='Year',palette='viridis')

# To relocate the legend
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)


# In[156]:


byMonth = df.groupby('Month').count()
byMonth.head()


# ** Now create a simple plot off of the dataframe indicating the count of kills per month. **

# In[157]:


byMonth['n_killed'].plot()


# ** Now create a simple plot off of the dataframe indicating the count of kills per Year. **

# In[159]:


byYear = df.groupby('Year').count()

byYear['n_killed'].plot()


# ** Now create a simple plot off of the dataframe indicating the count of injured per Year. **

# In[160]:


byYear = df.groupby('Year').count()

byYear['n_injured'].plot()


# ** Now create a HeatMap using this new DataFrame. **

# In[170]:


monthKill = df.groupby(by=['state','Month']).count()['n_killed'].unstack()
monthKill.head()


# In[174]:


plt.figure(figsize=(12,20))
sns.heatmap(monthKill,cmap='viridis')


# In[184]:

sns.clustermap(monthKill,cmap='viridis')




