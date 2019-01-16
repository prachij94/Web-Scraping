# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 12:28:03 2018

@author: Prachi Jain
"""

from lxml import html  
import json
import requests

url  = 'http://www.industrybuying.com/office-chairs-ib-basics-OFF.OFF.41380990/'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
page = requests.get(url,headers = headers,verify=False)
page_response = page.text
parser = html.fromstring(page.content)

productname = parser.xpath('//*[@id="main"]/div/div/div/div/div/div[1]/div[3]/div[2]/div[1]/span/h1')
name = productname[0].text_content().strip()

productspecs = parser.xpath('//*[@id="productSpecifications"]/table')
    
a = productspecs[0].text_content().strip().split('\n')


a = [x.strip(' ') for x in a]
a= list(filter(None,a))
a.remove(a[0])
data = dict(zip(a[::2], a[1::2]))
