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
driver.find_element_by_name('session_key').send_keys('e-mail')
driver.find_element_by_name('session_password').send_keys('password')
button = driver.find_elements_by_class_name('sign-in-form__submit-button')
button[0].click()
driver.get('https://www.linkedin.com/jobs/')

#use datetime for  ember 41&40 16h
driver.find_element_by_id('jobs-search-box-keyword-id-ember40').send_keys('field')
driver.find_element_by_id('jobs-search-box-location-id-ember40').send_keys('City')
driver.find_element_by_xpath('//button[normalize-space()="Recherche"]').click()
driver.find_element_by_xpath('//*[@id="ember72"]').click()
#driver.find_element_by_xpath('//*[text()="Vous êtes dans la fenêtre de messagerie. Appuyez sur Entrée pour la réduire."]/button').click()

Yeay = driver.find_element_by_css_selector('.job-card-list__entity-lockup.artdeco-entity-lockup.artdeco-entity-lockup--size-4.ember-view').text
print(Yeay)

#
description = driver.find_element_by_xpath('//*[@id="job-details"]').text
print(description)

#Recrutement actif isn't
JRP = driver.find_element_by_xpath('//*[text()="Recrutement actif"]/ancestor::div').text
driver.close()
test = JRP.split("\n")



'''
#remove the first section of web page : 
Eff = 'Candidature simplifiée'
for intro in test:
    if Eff in intro:
        break
    else:
        print(intro)
        test.remove(intro)
'''

#separate element : 
chunk = [[]]
sep = 'Sponsorisé'
brk = 'Le statut est en ligne'
i = 0
for val in test:
    if sep in val:
        i = i+1
        chunk.extend([[val]])
        #val.replace(sep, "")
    if brk in val:
        break
    else:
        chunk[i].extend([val])
        
print('Jobs : ', chunk, len(chunk))

for c in chunk:
    print(len(c))

'''

'''

