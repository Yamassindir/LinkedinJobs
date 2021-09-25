from selenium import webdriver
import os
import pandas as pd
import datetime
from selenium.webdriver.common.keys import Keys


#options
options = webdriver.ChromeOptions()
options.add_argument('--headless')
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)


driver = webdriver.Chrome('C:/Users/elaya/Downloads/chromedriver_win32/chromedriver.exe', options=options)

driver.implicitly_wait(10)
driver.get('https://www.linkedin.com/')
driver.maximize_window()
driver.find_element_by_name('session_key').send_keys('****yassir@gmail.com')
driver.find_element_by_name('session_password').send_keys('******')
button = driver.find_elements_by_class_name('sign-in-form__submit-button')
button[0].click()
driver.get('https://www.linkedin.com/jobs/')

#use datetime for  ember 41&40 16h
driver.find_element_by_id('jobs-search-box-keyword-id-ember40').send_keys('****')
driver.find_element_by_id('jobs-search-box-location-id-ember40').send_keys('****')
driver.find_element_by_xpath('//button[normalize-space()="Recherche"]').click()
driver.find_element_by_xpath('//*[@id="ember72"]').click()

#description
description = driver.find_element_by_css_selector('.jobs-search__right-rail').text
print(description)

#Recrutement actif isn't
JRP = driver.find_element_by_css_selector('ul.jobs-search-results__list.list-style-none').text 
driver.close()
test = JRP.split("\n")



#remove the first section of web page : 
Eff = ['Sponsorisé', 'Recrutement actif']
for intro in test:
    if any(Eff):
        test.remove(intro)

#separate element : 
chunk = [[]]
sep = ', France'
brk = 'Le statut est en ligne'
i = 0
for val in test:
    if sep in val:
        i = i+1
        chunk.extend([[val]])
    if brk in val:
        break
    else:
        chunk[i].extend([val])
        
Toxcl = pd.DataFrame(chunk)

Toxcl.to_excel("LinkedIn.xlsx", header=False, index=False)


'''
Toxcl.to_excel("LinkedIn.xlsx",
             sheet_name="sheet1",
             startrow=len(chunk),
             startcol=0)
'''



