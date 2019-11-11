#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests
import os


# In[2]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# visit the mars.nasa.gov site
url = ('https://mars.nasa.gov/news/')
browser.visit(url)




# # Scraping 
# 

# ### NASA Mars News

# In[6]:


# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. 
# Assign the text to variables that you can reference later.


# In[4]:


html = browser.html
soup = BeautifulSoup(html, "html.parser")
slide_element = soup.select_one("ul.item_list li.slide")


# In[5]:


slide_element.find("div",class_="content_title")


# In[6]:


print(soup.prettify())



# In[7]:


#news_para = latestarticle.find("div", class_="article_teaser_body").text
title = soup.title
title


# In[8]:


# Most Recent Title

latest_title = slide_element.find("div", class_="content_title").get_text()
print(latest_title)


# In[9]:


#Most Recent Title's paragraph

paragraph = slide_element.find("div", class_="article_teaser_body").get_text()
print(paragraph)


# In[10]:


# Most Recent Title's Date

date = slide_element.find("div", class_="list_date").get_text()
print(date)


# In[11]:


print("The Most Recent NASA News:")
print("----------------------")
print(latest_title)
print(date)
print(paragraph)


# ### JPL Mars Space Images - Featured Image

# In[12]:


# Visit the url for JPL Featured Space Image here.
# Use splinter to navigate the site and find the image url for the current 
# Featured Mars Image and assign the url string to a variable called featured_image_url.
# Make sure to find the image url to the full size .jpg image.
# Make sure to save a complete url string for this image.

##looked to github for code help: sharonsu94


# In[13]:


# Visit the url for JPL Featured Space Image here.

executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path)
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, "html.parser")


# In[14]:


# Use splinter to navigate the site and find the image url for the current 
# Featured Mars Image and assign the url string to a variable 
# called featured_image_url.

featured_image = soup.find("img", class_="thumb")["src"]
featured_image_url = "https://www.jpl.nasa.gov" + featured_image
print(featured_image_url)


# ### Mars Weather
# 

# In[15]:


## Visit the Mars Weather twitter account here and scrape the latest Mars weather 
# tweet from the page. Save the tweet text for the weather report as a variable 
# called mars_weather.


# In[16]:


url = ("https://twitter.com/marswxreport?lang=en")
browser = Browser("chrome", **executable_path)



# In[17]:


executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path)
url = "https://twitter.com/marswxreport?lang=en"
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, "html.parser")


# In[18]:


#html = browser.html
#soup = BeautifulSoup(html, 'html.parser')

mars_weather_tweet = soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})

#response = requests.get(url)


# In[19]:


##LATEST MARS WEATHER TWEET##

mars_weather = mars_weather_tweet.find('p', 'tweet-text').get_text()
mars_weather


# In[20]:


#print(soup.prettify())


# In[21]:


#content = soup.find_all("div", class_="content")
#print(content)


# ### Mars Facts

# In[22]:


## Visit the Mars Facts webpage here and use Pandas to scrape the table containing 
## facts about the planet including Diameter, Mass, etc.
## Use Pandas to convert the data to a HTML table string.

##used github: Bigbluey for some help with reading the table


# In[23]:


executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path)
url = "https://space-facts.com/mars/"
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, "html.parser")
table = soup.find('table', attrs={'class': 'widget widget_text profiles'})


# In[24]:


mars_facts_table_df = pd.read_html("https://space-facts.com/mars/")[0]
print(mars_facts_table_df)


# In[25]:


mars_facts_table_df.columns=["Description", "Value"]
mars_facts_table_df.set_index("Description", inplace=True)
mars_facts_table_df


# ### Mars Hemispheres
# 

# In[26]:


# Visit the USGS Astrogeology site here to obtain high resolution images for each 
#   of Mar's hemispheres.
# You will need to click each of the links to the hemispheres in order to find the 
#   image url to the full resolution image.
# Save both the image url string for the full resolution hemisphere image, and the 
#  Hemisphere title containing the hemisphere name. Use a Python dictionary to store 
#  the data using the keys img_url and title.
# Append the dictionary with the image url string and the hemisphere title to a list. 
#  This list will contain one dictionary for each hemisphere.


# In[38]:


executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path)
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, "html.parser")


# In[39]:


image_urls = []

hemisphere_image_titles = soup.find_all('h3')

for hemisphere in hemisphere_image_titles:
    hemisphere_image_titles.append(hemisphere.text)

hemisphere_image_titles


# In[40]:


hemisphere_image_urls = []

links = soup.find_all("div", class_="item")

#loop through each url to get the image 
for link in links:
    ##start the dictionary
    hemisphere_dict = {}
    
    #click on the links
    next_link = link.find("div", class_="description").a["href"]
    next_next_link = url + next_link
    
    
    #click on the next link
    browser.visit(next_next_link)
    
    pic_html = browser.html
    pic_soup = BeautifulSoup(pic_html, 'html.parser')
    
    pic_url = pic_soup.find("img", class_="wide-image")["src"]
     
    #scrape img url string and store dict
    hemisphere_dict["hemisphere_image_titles"] = hemisphere_image_titles
    hemisphere_dict["img_url"] = url + pic_url

    print(hemisphere_dict["img_url"])
    
    hemisphere_image_urls.append(hemisphere_dict)
    
    
    #store hemisphere title to the dict
  ####  hemisphere_dict["title"] = hemisphere
    
    #add dict to image urls
  ###  image_urls.append(hemisphere_dict)
    
 ##   pprint(image_urls)
    
 ##   browser.click_link_by_partial_text('Back')


# In[29]:


##Github ninoyosinao was used for some help understanding


# In[35]:


print(hemisphere_image_urls)


# In[ ]:




