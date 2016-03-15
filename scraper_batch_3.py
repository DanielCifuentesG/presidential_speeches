
# coding: utf-8

# Author: Santiago Matallana
# 
# Project: Presidential speeches
# 
# Created: 2016-03-13
# 
# Purpose: Scrape batch 3 of speeches, from JavaScript rendered website.

# ---

# In[31]:

# Requirements

import re
import pandas as pd
import selenium
from selenium import webdriver
chrome_path = r'/Applications/chromedriver'


# In[32]:

driver = webdriver.Chrome(chrome_path)


# In[33]:

# Home

driver.get('http://es.presidencia.gov.co/discursos')


# In[34]:

speeches_1 = driver.find_elements_by_class_name("mtmL-Titulo")
len(speeches_1)


# In[35]:

text = []
for speech in speeches_1:
    text.append(speech.text)
len(text)


# In[36]:

urls = []
for speech in speeches_1:
    urls.append(speech.find_element_by_css_selector('a').get_attribute('href'))
len(urls)


# ---

# In[37]:

# Page 2

driver.find_element_by_xpath("""//*[@id="ctl00_ctl51_g_463cfee5_deb2_4d62_8ba8_e9006779ac49_csr"]/ul/li[1]/span/a[2]""").click()


# In[38]:

speeches_2 = driver.find_elements_by_class_name("mtmL-Titulo")
len(speeches_2)


# In[39]:

for speech in speeches_2:
    text.append(speech.text)
len(text)


# In[40]:

for speech in speeches_2:
    urls.append(speech.find_element_by_css_selector('a').get_attribute('href'))
len(urls)


# ---

# In[41]:

# Page 3

driver.find_element_by_xpath("""//*[@id="ctl00_ctl51_g_463cfee5_deb2_4d62_8ba8_e9006779ac49_csr"]/ul/li[1]/span/a[2]""").click()


# In[42]:

speeches_3 = driver.find_elements_by_class_name("mtmL-Titulo")
len(speeches_3)


# In[43]:

for speech in speeches_3:
    text.append(speech.text)
len(text)


# In[44]:

for speech in speeches_3:
    urls.append(speech.find_element_by_css_selector('a').get_attribute('href'))
len(urls)


# ---

# In[45]:

# Page 4

driver.find_element_by_xpath("""//*[@id="ctl00_ctl51_g_463cfee5_deb2_4d62_8ba8_e9006779ac49_csr"]/ul/li[1]/span/a[2]""").click()


# In[46]:

speeches_4 = driver.find_elements_by_class_name("mtmL-Titulo")
len(speeches_4)


# In[47]:

for speech in speeches_4:
    text.append(speech.text)
len(text)


# In[48]:

for speech in speeches_4:
    urls.append(speech.find_element_by_css_selector('a').get_attribute('href'))
len(urls)


# ---

# In[49]:

# Page 5
driver.find_element_by_xpath("""//*[@id="ctl00_ctl51_g_463cfee5_deb2_4d62_8ba8_e9006779ac49_csr"]/ul/li[1]/span/a[2]""").click()


# In[50]:

speeches_5 = driver.find_elements_by_class_name("mtmL-Titulo")
len(speeches_5)


# In[51]:

for speech in speeches_5:
    text.append(speech.text)
len(text)


# In[52]:

for speech in speeches_5:
    urls.append(speech.find_element_by_css_selector('a').get_attribute('href'))
len(urls)


# ---

# In[53]:

# Page 6
driver.find_element_by_xpath("""//*[@id="ctl00_ctl51_g_463cfee5_deb2_4d62_8ba8_e9006779ac49_csr"]/ul/li[1]/span/a[2]""").click()


# In[54]:

speeches_6 = driver.find_elements_by_class_name("mtmL-Titulo")
len(speeches_6)


# In[55]:

for speech in speeches_6:
    text.append(speech.text)
len(text)


# In[56]:

for speech in speeches_6:
    urls.append(speech.find_element_by_css_selector('a').get_attribute('href'))
len(urls)


# In[57]:

text


# In[58]:

urls


# ---

# ### From the list 'text', extract the location, date, and title of the speech, and from the list 'urls', scrape the body of the speech.

# In[74]:

def get_info(text):
    year = re.findall(r'([0-9]{4})\n', text)[0]
    month = re.findall('[0-9]+ de (.+) de ' + year[0], text)[0]
    day = re.findall('([0-9]+) de ' + month[0], text)[0]
    title = re.findall(r'\n(.+)', text)[0]
    location = re.findall('(.+), [a-z].+' + day[0], text)[0]
    return [year, month, day, title, location]


# In[79]:

corpus3_elements = list(map(get_info, text))
len(corpus3_elements)


# In[90]:

# Create Pandas dataframe

corpus3_df = pd.DataFrame(corpus3_elements, columns = ["Year", "Month", "Day", "Title", "Location"])
corpus3_df


# In[91]:

# Relabel months with numbers, using same format as batches 1 and 2

months = {'enero':'01','febrero':'02','marzo':'03','abril':'04','mayo':'05','junio':'06','julio':'07','agosto':'08',          'septiembre':'09','octubre':'10','noviembre':'11','diciembre':'12'}


# In[92]:

# For each value in 'Month', apply function that labels with corresponding number

corpus3_df['Month'] = corpus3_df['Month'].apply(lambda x: months[x])


# In[93]:

corpus3_df


# In[94]:

from scraper_helper import get_html, get_speech, remove_tags


# In[95]:

def get_speech_text(url):
    return remove_tags(get_speech(get_html(url)))


# In[96]:

speeches3 = list(map(get_speech_text, urls))
len(speeches3)


# In[97]:

corpus3_df['URL'] = urls
corpus3_df['Speech'] = speeches3


# In[98]:

corpus3_df


# In[99]:

corpus3_df.to_pickle('speeches_df_batch3.pkl')

