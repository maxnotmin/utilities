#!/usr/bin/env python3
from collections import OrderedDict

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


#Works with Chrome 64
#using ChromeDriver 2.7
CHROME_LOC = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
CHROME_DRIVER = r'chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument("--headless")
#chrome_options.binary_location = CHROME_LOC

driver = webdriver.Chrome(executable_path=CHROME_DRIVER, chrome_options=chrome_options)
driver.get("https://www.python.org/")
print("AFTER DRIVER")
the_body = driver.find_element_by_id("homepage")

print("the body : homepage id: ", the_body.text)

the_about = driver.find_element_by_id("about")
print("The About: ", the_about.text)
if the_about.is_displayed():
    the_about.click()
else:
    the_community = driver.find_element_by_id("community")
    the_community.click()

driver.close()
