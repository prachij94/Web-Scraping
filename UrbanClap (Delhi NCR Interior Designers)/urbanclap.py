# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:31:20 2018

@author: prachi
"""
#Importing the required packages to make url requests using requests,automation using Selenium and scraping functionalities with the help of BeautifulSoup
import requests
import time as t
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

#Saving the url and finding if we are successful(code 200) in getting the response. If not, exiting the code
endpoint = "https://www.urbanclap.com/delhi-ncr-interior-designers"
response = requests.get(endpoint)
if response.status_code != 200:
        print('Failed to retrieve articles with error {}'.format(response.status_code))
        exit()

#Assigning the options with which the automated browser window opens up
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--start-maximized")
options.add_argument("--test-type")
#options.add_argument("--headless")


designerinfo = []
locationinfo = []
url=endpoint
j=1
row=0

#Creating an empty dataframe to store the fetched information
outputinfo = pd.DataFrame(columns={'Designer Name','Location'})

#Looping in the range of different urls ranging from https://www.urbanclap.com/delhi-ncr-interior-designers?p=2 to https://www.urbanclap.com/delhi-ncr-interior-designers?p=350
for j in range(2,351):

	#Create a chrome driver for automated browser, the chromedriver.exe file should be present the system for providing the functionality for a Chrome browser and similarly geckodriver.exe for a firefox browser
        driver = webdriver.Chrome(executable_path='C:/Users/prachi/Downloads/chromedriver_win32/chromedriver.exe',chrome_options=options)
        t.sleep(3)
            #driver = webdriver.Firefox(executable_path='C:/Users/imart/Downloads/geckodriver-v0.21.0-win64/geckodriver.exe')
        driver.get(url)
        
        t.sleep(5)
        
	#Opening and closing a new browser window driver2 briefly so that the mouse focus shifts from driver1 and popup appears in driver1 and we can close it later
        driver2 = webdriver.Chrome(executable_path='C:/Users/prachi/Downloads/chromedriver_win32/chromedriver.exe',chrome_options=options)
        t.sleep(2)
        driver2.quit()
        
        #Closing the popup by clicking on close button in it
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div/section/div/div/div/div/span').click()
        
        
        #Creating a soup object from BeautifulSoup and using it to find the required elements in the html page
        source_data = driver.page_source
        soup = BeautifulSoup(source_data, "html.parser")
        l=[]
        x = soup.find_all('div',attrs={'class':'QARuRXdTfrs1BseXGeV56'})
        for abc in x:
            print(abc.contents[0].text)
            print(abc.text)
            name = abc.contents[0].text
            eg = (abc.text).replace(abc.contents[0].text,'')
            l = eg.split(' (')
            l = l[0]
            l = l.split('1.')
            l = l[0]
            l = l.split('2.')
            l = l[0]
            l = l.split('3.')
            l = l[0]
            l = l.split('4.')
            l = l[0]
            l = l.split('5.')
            l = l[0]
        

                    
            
            outputinfo.set_value(row,'Designer Name',name)
            outputinfo.set_value(row,'Location',l)
            row=row+1
        url = endpoint+'?p='+str(j)
        
        driver.quit()
        
outputinfo.to_csv('DelhiUrbanclap.csv',index=False)
