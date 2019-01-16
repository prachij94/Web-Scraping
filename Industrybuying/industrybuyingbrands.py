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
finaldf = pd.DataFrame(columns=['Category','Brand'])

#Opening a browser window and navigating to the url
driver = webdriver.Chrome(executable_path='C:/Users/prachi/Downloads/chromedriver.exe',chrome_options=options)

driver.get('https://www.industrybuying.com/all-brands/')

# Applying a time delay for allowing the page to load completely
t.sleep(2)



#finding the category names and links to the category brand-wise pages
categorieslist = driver.find_element_by_class_name('categorylist')
categorylinks=categorieslist.find_elements_by_tag_name('a')
categorynames = [e.text for e in categorylinks]
categories=[e.get_attribute('href') for e in categorylinks]


row=0


#Iterating over categories and finding all the corresponding brands against each one
for c in range(0,len(categories)):
    driver.get(categories[c])
    t.sleep(2)
    
    brandlinks=(driver.find_element_by_class_name('numberlist')).find_elements_by_tag_name('a')
    brands = [b.text for b in brandlinks]    
    
    
    #Writing the category and brands for them into a result df
    for j in range(0,len(brands)):
        finaldf.set_value(row,'Category',categorynames[c])
        finaldf.set_value(row,'Brand',brands[j])
        
        row=row+1

#Exporting the results into an excel sheet        
finaldf.to_csv('IndustryBuyingCategorywiseBrands.csv',index=False)
