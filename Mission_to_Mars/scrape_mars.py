from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import flask
import pandas as pd
import splinter as spl



def scrape():
    marsdict = {}
    
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    # Visit redplanetscience.com
    url = "https://redplanetscience.com/"
    browser.visit(url)
    
    # Scrape page into soup
    html = browser.html
    soup = bs(html, "html.parser")
    
    # Get the article title and paragraph.
    news_title = soup.find('div', class_ = 'content_title').text.strip()
    news_p = soup.find('div', class_ = 'article_teaser_body').text.strip()
    
    marsdict['title'] = news_title
    marsdict['paragraph'] = news_p
    
    browser.quit()
    
   
  
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    
    # Scrape page into soup
    html = browser.html
    soup = bs(html, "html.parser")
    
    # Get the featured image
    images = soup.find('div', class_='header')
    link = images.find_all('img')[1]
    href = link['src']
    featured_image_url ='https://spaceimages-mars.com/' + href
    marsdict['featured'] = featured_image_url
    browser.quit()
    
    url = 'https://galaxyfacts-mars.com/'
    df = pd.read_html(url)[1]
    mars_table = df.to_html()
    mars_table.replace('\n', '')
    marsdict['table'] = mars_table
    
    
    
    # Create a list to loop through the image links
    links = ['cerberus',
            'schiaparelli',
            'syrtis',
            'valles']
    # Fill buckets with data
    hemisphere_titles = []
    hemisphere_urls = []

    for link in links:
    # Visit spaceimages-mars.com
            executable_path = {'executable_path': ChromeDriverManager().install()}
            browser = Browser('chrome', **executable_path, headless=False)
            url = (f"https://marshemispheres.com/{link}.html")
            browser.visit(url)

            # Scrape page into soup
            html = browser.html
            soup = bs(html, "html.parser")
            
            # Get the hi-res images
            images = soup.find('div', class_='downloads')
            click = images.find_all('a')[1]
            href = click['href']
            imgurl ='https://marshemispheres.com/' + href
            hemisphere_urls.append({"img_url": imgurl})
           
          # Get titles
            title = soup.find('div', class_='cover')
            h2 = title.find('h2', class_='title').text.strip()
            hemisphere_titles.append({'title': h2})

            browser.quit()
            
            
            
            hemisphere_image_urls = [
                {'title1': 'Cerberus Hemisphere Enhanced', 'img_url1': 'https://marshemispheres.com/images/cerberus_enhanced.tif'},
                {'title2': 'Schiaparelli Hemisphere Enhanced', 'img_url2': 'https://marshemispheres.com/images/schiaparelli_enhanced.tif'},
                {'title3': 'Syrtis Major Hemisphere Enhanced', 'img_url3': 'https://marshemispheres.com/images/syrtis_major_enhanced.tif'},
                {'title4': 'Valles Marineris Hemisphere Enhanced', 'img_url4': 'https://marshemispheres.com/images/valles_marineris_enhanced.tif'}
            ]
            
            marsdict['images'] = hemisphere_image_urls

    return listings
