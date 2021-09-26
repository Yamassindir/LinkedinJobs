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
driver.get('https://www.linkedin.com/jobs/')
driver.maximize_window()
driver.find_element_by_name('keywords').send_keys('Business Intelligence') 
loc = driver.find_element_by_name('location')
driver.execute_script("arguments[0].value = ''", loc)
loc.send_keys('Paris')
loc.send_keys(Keys.RETURN)



#accept cookies : 
driver.find_element_by_xpath('//button[normalize-space()="Accepter les cookies"]').click()
#driver.find_element_by_xpath('//button[normalize-space()="Afficher plus"]').click()


#description
description = driver.find_element_by_css_selector('.decorated-job-posting__details').text
#print(description)


# Get text from all elements
Job_List = [el.text for el in driver.find_elements_by_xpath('//ul[@class="jobs-search__results-list"]/li')]

driver.close()

# Print text
#[list(job.split("\n")) for job in Job_List]
j_l = [["Job title", "Company", "Location", "Number of candidates", "History"]]
for job in Job_List:
    job = list(job.split("\n"))
    j_l.extend([job])

Toxcl = pd.DataFrame(j_l)
Toxcl.to_excel("LinkedIn.xlsx", header=j_l[0], startrow=1, index=False)

print('end')

