# -*- coding: utf-8 -*-
"""Headline Scrapping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-MmtJLDVoXCCpuyrLlWRxm4-zrUoPziy
"""

!pip install urllib3

# Run in the PyCharm or Spyder or other IDE for results 

import requests
from bs4 import BeautifulSoup
import csv

def beautiful_soup(url):
    '''DEFINING THE FUNCTION HERE THAT SENDS A REQUEST AND PRETTIFIES THE TEXT 
       INTO SOMETHING THAT IS EASY TO READ'''

    request = requests.get(url)
    soup = BeautifulSoup(request.text, "lxml")
    return soup

soup = beautiful_soup('https://www.hindustantimes.com/top-news')

with open('output.csv', 'w', newline='', encoding='utf-8') as f_output:
    csv_output = csv.writer(f_output)
    #csv_output.writerow(['Headline'])

    for headlines in soup.find_all('div', {'class': 'media-heading headingfour'}):
        headline = headlines.find_next('a').text
        print(headline)
        csv_output.writerow([headline])

        # Run in the PyCharm or Spyder or other IDE for results