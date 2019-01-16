# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 13:24:56 2019

@author: prachi
"""


#Importing libraries
from selenium import webdriver
import pandas as pd
import time as t

'''  For Google Chrome browser'''
options = webdriver.ChromeOptions()

''' For Firefox browser'''
#options = webdriver.FirefoxOptions()


#Adding options for the browser to be opened
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--start-maximized")
options.add_argument("--headless")




#Creating an empty dataframe to store the scraped information
finaldf = pd.DataFrame(columns=['Category','Subcategory','MinPrice','MaxPrice','Brand(WithCount)'])

#Opening a browser window and navigating to the url
driver = webdriver.Chrome(executable_path='C:/Users/prachi/Downloads/chromedriver.exe',chrome_options=options)

driver.get('https://www.industrybuying.com/all-brands/')

# Applying a time delay for allowing the page to load completely
t.sleep(2)



#finding the category names and links to the category brand-wise pages
categorieslist = driver.find_element_by_class_name('categorylist')
categorylinks=categorieslist.find_elements_by_tag_name('a')
categorynames = [e.text for e in categorylinks]



row=0   #initiatilaising result dataframe row 0
cat_to_subcatlinks={}   #Creating a dictionary which maps category name to the http links of subcategories in each category
cat_to_subcatnames={}   #Creating a dictionary which maps category name to the subcategory names in each category


#Navigating to the categories page
driver.get('https://www.industrybuying.com/categories/')
t.sleep(2)

#Finding all the subcategories inside each category
subcatdivs=driver.find_elements_by_class_name('categories_links')



#Extracting the subcategory names and subcategory links for each category and storing in the above dictionaries    
for subcats in range(0,len(subcatdivs)):
    
    subcatnames = [n.text for n in subcatdivs[subcats].find_elements_by_class_name('cat_c1')]
    subcatlinks = [l.find_element_by_tag_name('a').get_attribute('href') for l in subcatdivs[subcats].find_elements_by_class_name('cat_c1')]
    
    cat_to_subcatnames[categorynames[subcats]] = subcatnames
    cat_to_subcatlinks[categorynames[subcats]] = subcatlinks
    
    
    

#Iterating over subcategory links stored for each category in the above dictionary
#Finding the Subcategory min and maximum price ranges and all the brands list along with their product counts
#Set the extracted data into a result df         
for i in range(0,len(cat_to_subcatlinks)):
    print(list(cat_to_subcatlinks.keys())[i])
    subcatpagelinks = cat_to_subcatlinks[list(cat_to_subcatlinks.keys())[i]]
    subcatnames = cat_to_subcatnames[list(cat_to_subcatnames.keys())[i]]
    
    for j in range(0,len(subcatpagelinks)):
        print(j)
        subcatname = cat_to_subcatnames[list(cat_to_subcatnames.keys())[i]][j]
        driver.get(subcatpagelinks[j])
        t.sleep(2)
        
        try:
            minprice=driver.find_element_by_id('minPriceInput').get_attribute('value')
        except:
            minprice = 'No price available'
        try:
            
            maxprice=driver.find_element_by_id('maxPriceInput').get_attribute('value')
        except:
            maxprice = 'No price available'
        
        try:
            brands = [b.text for b in ((driver.find_element_by_id('filter_name_brand_id')).find_elements_by_tag_name('span'))]
        except :
            try:
                brands = [b.get_attribute('href').split('/')[4] for b in ((driver.find_element_by_class_name('carousel-inner')).find_elements_by_tag_name('a'))]
            except:    
                brands = 'No Products found'
                finaldf.set_value(row,'Category',list(cat_to_subcatlinks.keys())[i])
                finaldf.set_value(row,'Subcategory',subcatname)
                finaldf.set_value(row,'Brand(WithCount)',brands)
                finaldf.set_value(row,'MinPrice',minprice)
                finaldf.set_value(row,'MaxPrice',maxprice)
                
                row=row+1
                continue
                
        for brand in brands:
            finaldf.set_value(row,'Category',list(cat_to_subcatlinks.keys())[i])
            finaldf.set_value(row,'Subcategory',subcatname)
            finaldf.set_value(row,'Brand(WithCount)',brand)
            finaldf.set_value(row,'MinPrice',minprice)
            finaldf.set_value(row,'MaxPrice',maxprice)
            
            row=row+1
            
driver.quit()            
#Exporting the results into an excel sheet        
finaldf.to_csv('IndustryBuyingSubcatwiseWithPriceRange.csv',index=False)
