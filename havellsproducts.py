# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 09:58:32 2018

@author: prachi
"""

from lxml import html  
import requests
from bs4 import BeautifulSoup
import re

url  = 'https://www.havells.com/en/consumer/fans/ceiling-fans/premium-underlight/momenta-(1).html'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
page = requests.get(url,headers = headers,verify=False)
page_response = page.text
parser = html.fromstring(page.content)
productname = parser.xpath('//*[@id="form"]/section/div[1]/div/div[2]/header')[0].text_content().strip()
productname =re.sub(' +', ' ',productname).split('\n \n')

productdesc = parser.xpath('//*[@id="form"]/section/div[1]/div/div[2]/div[1]')[0].text_content().strip().split('\n')

soupvar = BeautifulSoup(page.content, "html.parser")
productname = soupvar.find_all('header')
productname = soupvar.find_all('div',attrs={'class':'pro-detail'})[0]
