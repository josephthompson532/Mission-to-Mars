# Mission-to-Mars

## Purpose
The purpose of this project was to impress Nasa employers by scraping from various pages of their website useful images and text and placing them on one page using Flask. At the click of a button, all of the latest updates to the sight can be scraped and displayed in one place for convenient review.

### Overview
In this project I scraped information and images from the nasa.gov website and displayed them in a Flask app that I created. To do this I incorporated a Mongo database, BeautifulSoup, Splinter as well as an index.html file to style and display my scraped data. First we created the database in mongo and connected it to our flask application. Then we wrote code in a separate scraping.py file that would, at the click of a button, rescrape all of the most recent nasa.gov data. We did this by defining a series of functions, which were all called when a scrape_all() function was called:

<img width="504" alt="Screen Shot 2020-10-02 at 12 53 37 PM" src="https://user-images.githubusercontent.com/66881241/94964253-5c0b5800-04ae-11eb-8d4c-a6cc5da4e54f.png">


We then imported this function into our flask app (app.py) and set up our code to run this function whenever the "scrape" button was pressed on our index.html page.


<img width="658" alt="Screen Shot 2020-10-02 at 12 53 50 PM" src="https://user-images.githubusercontent.com/66881241/94964246-59a8fe00-04ae-11eb-8404-f1485cdfed90.png">


To do the actual scraping we used splinter to navigate to webpages and save the html to a variable. Then we used Beautiful Soup to actually scrape the data from the HTML. This was done in our scraping.py file which was a collection of funtions that would return scraped data:

<img width="572" alt="Screen Shot 2020-10-02 at 12 50 51 PM" src="https://user-images.githubusercontent.com/66881241/94964065-f919c100-04ad-11eb-9885-4419891d6124.png">

The scraping.py file upon being run in app.py, would then be stored into a mongo database. The data would then be displayed in our HTML through accessing this mongo database.

## Results
The website is capable of all features I set out to apply to it. It successfully scrapes images, news, and even table information from nasa.gov and displays it in an easy to read format at the click of a single button.

### Snapshots of Parts of the website

![Screen Shot 2020-12-30 at 10 02 10 PM](https://user-images.githubusercontent.com/66881241/103396967-e5045080-4aea-11eb-80d0-0a07272ef7a9.png)

![Screen Shot 2020-12-30 at 10 02 51 PM](https://user-images.githubusercontent.com/66881241/103396971-e9306e00-4aea-11eb-9032-95ba0ea8488c.png)

![Screen Shot 2020-12-30 at 10 02 28 PM](https://user-images.githubusercontent.com/66881241/103396972-eafa3180-4aea-11eb-8a83-e3237877798f.png)
