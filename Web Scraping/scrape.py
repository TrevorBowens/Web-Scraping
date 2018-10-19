from splinter import Browser
import pymongo
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# Initialize browser
def init_browser():
  executable_path = {'executable_path': 'chromedriver'}
  browser = Browser('chrome', **executable_path, headless=False)
  print(browser)

# Function to scrape Mars websites
def scrape_article():

  #Initialize browser
  executable_path = {'executable_path': 'chromedriver'}
  browser = Browser('chrome', **executable_path, headless=False)
  article = {}

  print(browser)

  #NASA site
  nasa_url = 'https://mars.nasa.gov/news/8364/martian-skies-clearing-over-opportunity-rover/'
  browser.visit(nasa_url)
  twit_url = 'https://twitter.com/marswxreport?lang=en'
  browser.visit(twit_url)

  # Scrape page with soup
  response = requests.get(nasa_url)
  soup = bs(response.text, 'lxml')
  twit_response = requests.get(twit_url)
  twit_soup = bs(twit_response.text, 'lxml')

  #Scrape web for news title and paragraphs
  results = soup.find('div', class_='grid_layout')
  news_title = results.h1.text
  paragraphs = results.div.div.text

  twit_result = twit_soup.find('div', class_='js-tweet-text-container')

  # Store in dictionary  
  article = {
    "title": news_title,
    "paragraphs": paragraphs,
  }

  mars_weather = twit_result.find('p', class_='js-tweet-text').text

  #Return results
  return (article, mars_weather)


  #Visit Twitter
  twit_url = 'https://twitter.com/marswxreport?lang=en'
  browser.visit(twit_url)

  #Scrape page into soup
  twit_response = requests.get(twit_url)
  twit_soup = bs(twit_response.text, 'lxml')
  twit_result = twit_soup.find('div', class_='js-tweet-text-container')

  mars_weather = twit_result.find('p', class_='js-tweet-text').text
 
  
  return mars_weather

def mars_table():
  browser = init_browser()
  mars_url = 'https://space-facts.com/mars/'
  mars_planet_table = pd.read_html(mars_url)
  mars_df = mars_planet_table[0]
  mars_df.columns = ['Description', 'Measurement']
  mars_html_table = mars_df.to_html(index=False)
  mars_html_table.replace("\n", '')
  myfile = mars_df.to_html(index=False)
  return myfile

