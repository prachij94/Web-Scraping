# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 15:53:40 2018

@author: prachi
"""


from lxml import html  
import requests
from bs4 import BeautifulSoup

url  = 'https://spareshub.com/shock-absorber-rear-2wd-scorpio-tc-crde-m-hawk-eagle.html'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
page = requests.get(url,headers = headers,verify=False)
page_response = page.text
parser = html.fromstring(page.content)

productname = parser.xpath('//*[@id="product_addtocart_form"]/div[3]/div[1]/div[1]')
name = productname[0].text_content().strip()

soupvar = BeautifulSoup(page.content, "html.parser")
imglink = soupvar.find('a', attrs={'id': 'zoom1'})
img = imglink.get('href')
if(img.find('placeholder/default/')!=-1):
    img = "Default"

productprice = parser.xpath('//*[@id="product_addtocart_form"]/div[3]/div[1]/div[2]/div[1]/div')
price = productprice[0].text_content().strip()


productspecs = parser.xpath('//*[@id="product_addtocart_form"]/div[3]/div[3]')
    
a = productspecs[0].text_content().strip().split('\n')


a = [x.strip(' ') for x in a]
a= list(filter(None,a))
a=a[3:]
data = dict(zip(a[::2], a[1::2]))

productdesc = parser.xpath('//*[@id="collateral-tabs"]/dd[2]/div/div')
productdesc = productdesc[0].text_content().strip()
