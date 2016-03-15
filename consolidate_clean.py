
# coding: utf-8

# Author: Santiago Matallana
# 
# Project: Presidential speeches
# 
# Created: 2016-03-13
# 
# Purpose: Consolidate speeches (3 batches) and clean data

# ---

# In[42]:

# Requirements

import pandas as pd
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [18.0, 8.0]
import re
import string


# In[5]:

batch1 = pd.read_pickle('speeches_df_batch1.pkl')
batch1


# In[6]:

len(batch1)


# In[7]:

batch2 = pd.read_pickle('speeches_df_batch2.pkl')
batch2


# In[8]:

len(batch2)


# In[9]:

batch3 = pd.read_pickle('speeches_df_batch3.pkl')
batch3


# In[10]:

len(batch3)


# In[11]:

# Append batches in one dataframe

temp = batch1.append(batch2)
speeches = temp.append(batch3)
len(speeches)


# <div class="alert alert-success">
# **Cleaning**
# </div>

# In[14]:

# Strip speech from certain strings at the beginning and end

def clean_speech(text):
    return re.sub('.*?(SIG)|(Presidencia de la República de Colombia).*$|(Casa de Nariño).*$|    (Sistema Informativo de Gobierno)', '', text)


# In[15]:

speeches['Speech'] = speeches['Speech'].apply(clean_speech)


# In[16]:

speeches['Year'] = pd.to_numeric(speeches['Year'], errors = "coerce")
speeches['Month'] = pd.to_numeric(speeches['Month'], errors = "coerce")
speeches['Day'] = pd.to_numeric(speeches['Day'], errors = "coerce")


# In[18]:

# Inspect for errors

speeches.Year.sort_values()


# In[19]:

# Fix rows 752 and 1424

speeches.loc[752, 'URL']


# In[20]:

speeches.loc[1424, 'URL']


# In[21]:

speeches.loc[752, 'Year'] = 2012
speeches.loc[752, 'Month'] = 6
speeches.loc[752, 'Day'] = 23
speeches.loc[1424, 'Year'] = 2013
speeches.loc[1424, 'Month'] = 8
speeches.loc[1424, 'Day'] = 7


# In[22]:

# Format date as datetime object

speeches['Date'] = pd.to_datetime(speeches.Year * 10000 + speeches.Month * 100 + speeches.Day, format='%Y%m%d')


# In[24]:

speeches.Date[0:5]


# In[25]:

# Drop obvious duplicates (criterion 1)

speeches.drop_duplicates(subset = ('Title', 'Date'), inplace = True)
len(speeches)


# In[28]:

# Drop obvious duplicates (criterion 2)

speeches.drop_duplicates(subset = ('Speech'), inplace = True)
len(speeches)


# In[27]:

# Drop obvious duplicates (criterion 3)

speeches.drop_duplicates(subset = ('URL'), inplace = True)
len(speeches)


# Found 2669 - 2656 = 13 duplicates.

# In[29]:

# Sort by date

speeches.sort_values('Date', inplace = True)


# In[30]:

# Reset index

speeches.reset_index(inplace = True, drop = True)
speeches


# In[32]:

# Grab punctuation characters

string.punctuation


# In[33]:

# Add additional relevant found characters to strip punctuation

punctuation = string.punctuation + '–¡¿”“•\r´'
punctuation


# In[34]:

# Strip punctuation from string

def no_punct(string):
    transtable = string.maketrans('', '', punctuation)
    return string.translate(transtable)


# In[35]:

# Add column with no punctuation

speeches['no_punct'] = speeches['Speech'].apply(no_punct)


# In[36]:

# Lowercase

speeches['no_punct'] = speeches['no_punct'].apply(str.lower)


# In[37]:

speeches.no_punct[0]


# In[38]:

# Add column with speech column tokenized

speeches['tokens'] = speeches['no_punct'].apply(word_tokenize)


# In[39]:

speeches


# In[44]:

# Grab stopwords in Spanish

stopwords_esp = stopwords.words('spanish')


# In[45]:

# Eliminate stopwords in Spanish

def no_stopwords(tokens):
    return [w for w in tokens if w not in stopwords_esp]


# In[46]:

# Add column with speech column tokenized

speeches['no_stopwords'] = speeches['tokens'].apply(no_stopwords)


# In[47]:

# Add column with nltk.Text object

speeches['nltk_Text'] = speeches['no_stopwords'].apply(nltk.Text)


# In[48]:

speeches


# In[49]:

speeches.to_pickle('speeches.pkl')

