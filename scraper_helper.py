
# coding: utf-8

# Author: Santiago Matallana
# 
# Project: Presidential speeches
# 
# Created: 2016-03-13
# 
# Purpose: Helper functions to scrape speeches

# ---

# In[1]:

# Requirements

import requests
from bs4 import BeautifulSoup
import re


# In[2]:

# Constants

MONTHS = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',     'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
YEARS = ['2010', '2011', '2012', '2013', '2014', '2015']


# In[3]:

def get_html(url):
    '''
    Requests url and parses text. Returns Beautiful Soup object.
    '''
    resp = requests.get(url).text
    return BeautifulSoup(resp,"lxml")


# In[4]:

def get_links(soup, regex):
    '''
    Extracts url links to speeches. Returns a list of urls of speeches.
    '''
    links = soup.find_all('a')
    return re.findall(regex, str(links))


# In[5]:

def links_speeches(main_urls, regex):
    '''
    Makes a list with the links to all speeches.
    '''
    speeches_urls = []
    for url in main_urls:
        soup = get_html(url)
        urls = get_links(soup, regex)
        speeches_urls = speeches_urls + urls
    return speeches_urls


# In[6]:

def get_date(speech_url):
    '''
    Returns year, month, and day from url
    '''
    date = re.findall('Paginas/(.{8})', speech_url)[0]
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]
    return year, month, day


# In[7]:

def get_title(soup):
    '''
    Returns title of speech
    '''
    return soup.title.text.strip()


# In[8]:

def get_speech(soup):
    '''
    Returns text of speech
    '''
    return str(soup.find_all('p'))


# In[9]:

def get_location(soup):
    '''
    Returns location of speech
    '''
    text = soup.p.text
    str1 = 'id="ctl00_PlaceHolderMain_ctl05__ControlWrapper_RichHtmlField" style="display:inline">'
    str2 = 'id="ctl00_PlaceHolderMain_content__ControlWrapper_RichHtmlField" style="display:inline"><p>'
    if len(re.findall('(.+), [0-9].+', text)) != 0:
        location = re.findall('(.+), [0-9].+', text)[0]
    elif len(re.findall(str1 + '(.+), [0-9].+', str(soup))) != 0:
        location = re.findall(str1 + '(.+), [0-9].+', str(soup))[0]
    elif len(re.findall(str2 + '(.+), [0-9].+', str(soup))) != 0:
        location = re.findall(str2 + '(.+), [0-9].+', str(soup))[0]
    else:
        location = 'N.A.'
    location = location.strip('<strong>')
    return location


# In[10]:

def remove_tags(text):
    '''
    Strips text from html and other tags
    '''
    return re.sub('<[^>]+>|\]|\[|\\u200b|\\n|\xa0', '', text)


# In[12]:

def get_speech_elements(speech_url):
    '''
    Returns
    '''
    print('Speech url: ', speech_url)
    soup = get_html(speech_url)
    title = get_title(soup)
    year, month, day = get_date(speech_url)
    speech = remove_tags(get_speech(soup))
    location = get_location(soup)
    return [year, month, day, title, location, speech_url, speech]

