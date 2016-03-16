
# Analysis of the speeches given by the President of Colombia, Juan M. Santos, from August 2010 to March 2016

[Santiago Matallana](http://www.santiagomatallana.com) - [About me](https://github.com/smatallana/resume_docs/blob/master/Santiago%20Matallana%20-%20Resume.pdf)

15-Mar-2016

<img src="wordcloud/wordcloud.png">

---

## Description and motivation

Colombia’s Presidency makes public on its website the interventions/speeches that current President Juan Manuel Santos has given since he came to office in August 2010. For this project I scraped those texts (over 2,600 speeches) and analyzed them using text analysis tools in Python.

Some questions/issues that motivated the project are:

- President Santos is trying to end a near 50-year-old conflict with left-wing guerilla FARC. There is an ongoing peace process that started in October 2012. Does the data reflect that in any way?
- President’s in Colombia can be reelected for one four-year period, for a maximum of eight years in office. President Santos was reelected in mid 2014. As is typical, prior to elections a Law for Electoral Guarantees was enacted. That law limited the type of political events that President Santos could hold, such as inaugurations of public works. Does the data reflect that in any way?
- The right-wing opposition, led by Ex-President Alvaro Uribe, has fiercely attacked Santos’ government and the peace process in particular. Juan Manuel Santos was Uribe’s Defense Minister and got elected with the support of the Ex-President. To the face of the public they have distanced dramatically over the past six years. Does the data reflect that in any way?
- What is the relative importance of policy areas, in terms of mentions of key words, such as education, entrepreneurship, employment, poverty, innovation, etc.?
- How does the data reflect specific events such us the recent decrease in oil prices, the depreciation of the COP, the soccer World Cup, etc.
- What do basic descriptive statistics of the data tell us about the President's interventions.







## Methods used

1. Scraping
    - The President’s speeches are available online in three batches, from three different websites.
        - Batch 1: from 08/07/2010 to 08/06/2014 (1,873 speeches): http://wsp.presidencia.gov.co/Discursos
        - Batch 2: from 08/07/2014 to 12/12/2015 (678 speeches): http://wp.presidencia.gov.co/Discursos
        - Batch 3: Most recent ones –last date of scraping: 03/13/2016– (118 speeches): http://es.presidencia.gov.co/discursos
    - To scrape the two batches of older speeches I used the 'requests' and 'BeautifulSoup' libraries.
    - The recent batch is available in a JavaScript rendered site. I extracted all the available speeches using 'selenium' library and 'webdriver' with Chrome.
    - The Python code is available [here for batches 1 and 2](scraper_batches_1-2.ipynb) and [here for batch 3](scraper_batch_3.ipynb).
<br><br>
2. Extracting the data from 'BeatifulSoup' objects:
    - Both to scrape the raw text and to extract the data from it, I wrote helper functions to: get htmls; get urls to speeches; get year, month, and day information from the text; get the title of the speech; remove html tags; and get the location of the speech; get all the elements of a speech in a structured object.
    - Helper functions are available [here](scraper_helper.ipynb).
<br><br>
3. Managing, storing, and further cleaning the data:
    - I used 'Pandas' to create a data frame for each batch of speeches, and exported each to a 'pickle' file for storage.
    - I consolidated the three data frames into one and furthered cleaned the data using 'Pandas' methods, 'string' methods, regular expressions, etc.
    - Using 'string' and 'nltk' libraries I stripped speeches from punctuation, converted to lowercase, tokenized text, dropped stopwords (in Spanish), etc.
    - Code is available in [here](consolidate_clean.ipynb).


## Findings

All code for analysis available [here](speeches_analysis.ipynb).

- Number of unique speeches: 2,651.
- Number of days in office: 2,041.
- Number of days in which at least one speech was given: 1,442
- Maximum number of speeches in a day: 6 (twice)

Here some visualizations of key findings:

<img src="images/hist_daily.png">

<img src="images/line_month.png">

The vertical blue line indicates the month in which the Law of Electoral Guarantees was enacted. This law limited the President's  interventions, as he announced running for reelection.

<img src="images/paz_terroristas_month.png">

The vertical blue line indicates the official start of peace talks with FARC.

<img src="images/topics_total.png">

<img src="images/dispersion1.png">

<img src="images/dispersion2.png">

---
