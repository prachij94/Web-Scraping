# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 16:16:35 2018

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



#Creating an empty dataframe to store the scraped information
finaldf = pd.DataFrame(columns=['State','City','Locality','Dealer','Email','Mobile number'])


#Opening a browser window and navigating to the url
driver = webdriver.Chrome(executable_path='C:/Users/prachi/Downloads/chromedriver.exe',chrome_options=options)

driver.get('https://www.daikinindia.com/products-services/daikin-dealer-locator')

# Applying a time delay for allowing the page to load completely
t.sleep(2)


#Extracting all the state names in the states dropdown list
states=driver.find_element_by_id('state').get_property('options')
stateslist = [a.text for a in states]

row=0

#Iterating over all the combinations of states, cities and localities dropdown list
for i in range(22,len(stateslist)+1):
    driver.find_element_by_id('state')
    driver.find_element_by_xpath('//*[@id="state"]/option['+str(i)+']').click()
    
    t.sleep(3)
    
    
    #Extracting all the state names in the cities dropdown list
    cities=driver.find_element_by_id('city').get_property('options')
    citylist = [a.text for a in cities]
    
    
    for j in range(2,len(citylist)+1):
        driver.find_element_by_id('city').click()
        driver.find_element_by_xpath('//*[@id="city"]/option['+str(j)+']').click()
    
        t.sleep(3)
        
        
        
        #Extracting all the state names in the localities dropdown list
        localities=driver.find_element_by_id('locality').get_property('options')
        localitylist = [a.text for a in localities]
        
        driver.find_element_by_id('locality').click()
        
        t.sleep(3)
        
        if(len(localitylist)!=1):
            for k in range(2,len(localitylist)+1):
                driver.find_element_by_id('locality').click()
                driver.find_element_by_xpath('//*[@id="locality"]/option['+str(k)+']').click()
                
                t.sleep(2)
                
                
                #Clicking on the find dealers button
                driver.find_element_by_xpath('//*[@id="dealer-locator"]/div[5]/input').click()
                
                try:
                    emails = driver.find_elements_by_class_name('email_clas')
                    
                    emails=[e.text for e in emails]
                    emailids = ""
                    for e in emails:
                        emailids=emailids+" "+e
                    finaldf.set_value(row,'Email',emailids)
                except:
                    finaldf.set_value(row,'Email','No email')
                
                
                try:
                    
                    phone = driver.find_elements_by_class_name('mobile_class')
                    phone = [p.text for p in phone]
                    phonenums=""
                    for p in phone:
                        phonenums=phonenums+" "+p
                    finaldf.set_value(row,'Mobile number',phonenums)
                except:
                    finaldf.set_value(row,'Mobile number','No phone number available')
                
                #Setting the extracted information about dealer into the output dataframe
                finaldf.set_value(row,'State',driver.find_element_by_xpath('//*[@id="state"]/option['+str(i)+']').text)
                finaldf.set_value(row,'City',driver.find_element_by_xpath('//*[@id="city"]/option['+str(j)+']').text)
                finaldf.set_value(row,'Locality',driver.find_element_by_xpath('//*[@id="locality"]/option['+str(k)+']').text)
                try :
                    
                    finaldf.set_value(row,'Dealer',driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div[3]/div[2]').text)
                    
                except:
                    finaldf.set_value(row,'Dealer','No Dealers found')
                finally:
                    
                    row = row + 1


#finaldf['Mobile1'],finaldf['Mobile2']=finaldf['Mobile number'].str.split('|',expand=True)[0],finaldf['Mobile number'].str.split('|',expand=True)[1]
#finaldf.drop_duplicates(inplace=True)
#finaldf['Email'].str.split(' ',expand=True)
#Exporting the output dataframe as a csv file
finaldf.to_csv('DealersDaikin.csv',index=False)
