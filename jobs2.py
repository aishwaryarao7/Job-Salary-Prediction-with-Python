import requests
from requests import get
from requests.exceptions import RequestException
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time
import urllib
from urllib.request import urlopen

scrape_data = pd.read_csv('jobs.csv', index_col=0)
scrape_data.shape

scrape_data = scrape_data.drop_duplicates()
scrape_data.reset_index(drop=True, inplace=True)
scrape_data.shape



print(scrape_data['salary'].value_counts())

scrape_data.to_csv('jobs2.csv', encoding='utf-8')
