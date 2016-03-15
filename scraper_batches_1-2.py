
# coding: utf-8

# Author: Santiago Matallana
# 
# Project: Presidential speeches
# 
# Created: 2016-03-13
# 
# Purpose: Scrape batches 1 and 2 of speeches

# ---

# In[6]:

# Requirements

import pandas as pd
import re

import scraper_helper
from imp import reload
reload(scraper_helper)

from scraper_helper import MONTHS, YEARS, get_html, get_links, links_speeches, get_date, get_title, get_speech, remove_tags, get_speech_elements


# In[2]:

# Generate suffixes for main urls

years_months = []
for year in YEARS:
    for month in MONTHS:
        years_months.append(year + '/Paginas/' + month + '.aspx')


# # Batch 1: from 08/07/2010 to 08/06/2014

# In[3]:

# Generate list of main urls for batch 1, 
# by appending corresponding suffixes to root

main_urls1 = []
prefix = 'http://wsp.presidencia.gov.co/Discursos/'
for suffix in years_months[7:56]:  # From August 2010 to August 2014
    main_urls1.append(prefix + suffix)  


# In[4]:

# Get all urls of speeches

speeches_urls1 = links_speeches(main_urls1,     '"(http://wsp.presidencia.gov.co/Prensa/.+?)"')


# In[19]:

# Apply function to extract speech elements, to all urls

corpus1 = list(map(get_speech_elements, speeches_urls1))


# In[20]:

len(corpus1)


# In[21]:

# Create Pandas dataframe

corpus1_df = pd.DataFrame(corpus1,     columns = ["Year", "Month", "Day", "Title", "Location", "URL", 'Speech'])


# In[27]:

# Export to pickle file

corpus1_df.to_pickle('speeches_df_batch1.pkl')


# # Batch 2: from 08/07/2014 to 12/12/2015

# In[28]:

# Generate list of main urls for batch 2, 
# by appending corresponding suffixes to root

main_urls2 = []
prefix = 'http://wp.presidencia.gov.co/Discursos/'
for suffix in years_months[-17:]:  # August 2014 and later
    main_urls2.append(prefix + suffix)


# In[29]:

# Get all urls of speeches

speeches_urls2 = links_speeches(main_urls2,     '"(http://wp.presidencia.gov.co/Noticias/.+?)"')


# In[30]:

# Apply function to extract speech elements, to all urls

corpus2 = list(map(get_speech_elements, speeches_urls2))


# In[31]:

len(corpus2)


# In[32]:

# Create Pandas dataframe

corpus2_df = pd.DataFrame(corpus2,     columns = ["Year", "Month", "Day", "Title", "Location", "URL", 'Speech'])


# In[33]:

# Export to pickle file

corpus2_df.to_pickle('speeches_df_batch2.pkl')


# In[ ]:

corpus1_df


# In[ ]:



