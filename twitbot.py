# Twitter bot

import time
import requests
from bs4 import BeautifulSoup as bs
import tweepy as tp


url = "https://www.brainyquote.com/quote_of_the_day"
site_request = requests.get(url)

soup = bs(site_request.text,'html.parser')