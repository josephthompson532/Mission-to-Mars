#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd

# Path to chromedriver
get_ipython().system('which chromedriver')

# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=True)


# In[2]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[3]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[4]:


slide_elem.find("div", class_='content_title')


# In[5]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[6]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# In[7]:


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[8]:


# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[9]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[11]:


# find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[12]:


# Use the base url to create an absolute url
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# In[13]:


df = pd.read_html('http://space-facts.com/mars/')[0]

df.head()


# In[14]:


df.columns=['Description', 'Mars']
df.set_index('Description', inplace=True)
df


# In[15]:


df.to_html()


# In[16]:


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)


# In[17]:


# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# In[18]:


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# In[ ]:





# In[19]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[20]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
hemi_image = soup(html, 'html.parser')


for item in hemi_image.find_all("div", class_="item"):
    
    hemispheres= {}
    
    thumb_nail = item.select_one('h3').get_text()
    
    link = item.find('a', class_='itemLink product-item')['href']
    
    browser.visit(f'https://astrogeology.usgs.gov{link}')
    
    html = browser.html
    
    mysoup = soup(html, 'html.parser')
    
    downloads_img = mysoup.find('div', class_='downloads')
    
    img_url = downloads_img.find('a')['href']
    
    hemispheres['title']= thumb_nail
    hemispheres['url']= img_url
    
    hemisphere_image_urls.append(hemispheres)
    
    
    
    
   


# In[22]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[23]:


# 5. Quit the browser
browser.quit()


# In[ ]:




