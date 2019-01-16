# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 17:43:33 2018

@author: Prachi Jain
"""

import requests
from bs4 import BeautifulSoup
def scrape_flipkart(url, no_products):
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    data = soup.find_all("div", {"class":"product-unit unit-3 browse-product quickview-required"})
    product_name = []
    image_url = []
    price = []
    link = []
    for item in data:
        name = item.find_all("a",{"class":"fk-display-block"})[0]
        product_name.append(name.get("title"))
        image = item.find_all("img")[0]
    if image.get("data-src"):
        img_url = image.get("data-src")
    else:
        img_url = image.get("src")
        image_url.append(img_url)
        price1 = item.find_all("div",{"class":"pu-final font-dark-color fk-inline-block"})[0]
        price.append(price1.text.strip())
        link.append(name.get("href"))
    product_name_final = product_name[:no_products]
    image_url_final = image_url[:no_products]
    price_final = price[:no_products]
    link_final = link[:no_products]
    print(product_name_final)
    print(image_url_final)
    print(price_final)
    print(link_final)
if __name__ == '__main__':
    print("Starting Product population script...")
 
    print('\n\n----------------------Flipkart Scraping Script------------------------\n\n')
print('\nMens Watches\n')
scrape_flipkart('http://www.flipkart.com/watches/pr?p%5B%5D=facets.ideal_for%255B%255D%3DMen&p%5B%5D=sort%3Dpopularity&sid=r18&facetOrder%5B%5D=ideal_for&otracker=ch_vn_watches_men_nav_catergorylinks_0_AllBrands', 5)