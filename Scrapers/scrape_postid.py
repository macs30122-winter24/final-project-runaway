from selenium import webdriver

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import sys
import io

# Classes of LIHKG

#------ Left Panel (Search posts) -----
leftPanel_id = "leftPanel"
leftPanel_class = "C_300Fi04lLpFu_ZznJqq"
postTitles_class = "qoAmEqNpZRLf2KVKZ8DsC" # List of panels
# Need to manually scroll down to load posts
postTitle_class = "wQ4Ran7ySbKd8PdMeHZZR" # Contains title and link of selected post
year_class = "_37XwjAqVHtjzqzEtybpHrU" # Contains time, this is under class "vv9keWAXpwoonDah6rSIU"

#------ Right Panel (Post contents) -----
comment_class = '_36ZEkSvpdj_igmog0nluzh'

KeyWord = "投票"
url = "https://lihkg.com/search?q="+KeyWord+"&sort=score&type=thread"
browser = webdriver.Chrome(executable_path="/Users/jingzhixu/Parking Lot/MACSS/2024winter/30122/chromedriver")
browser.maximize_window()
browser.get(url)

els = browser.find_elements(By.CLASS_NAME, "wQ4Ran7ySbKd8PdMeHZZR")
browser.execute_script("arguments[0].scrollIntoView();", els[-1])

links = []
def infinite_scroll(driver):
    number_of_elements_found = 0
    while True:
        time.sleep(5)
        els = driver.find_elements(By.CLASS_NAME, "wQ4Ran7ySbKd8PdMeHZZR")
        if number_of_elements_found == len(els):
            # Reached the end of loadable elements
            for e in els:
                links.append([a.get_attribute("href") for a in e.find_elements_by_tag_name("a")])
            break

        try:
            time.sleep(5)
            driver.execute_script("arguments[0].scrollIntoView();", els[-1])
            number_of_elements_found = len(els)
            print(number_of_elements_found)
        
        except StaleElementReferenceException:
            # Possible to get a StaleElementReferenceException. Ignore it and retry.
            pass
        
infinite_scroll(browser)   

Links = []
for p in links:
    if p[0] not in Links:
        Links.append(p[0])

len(Links)

filename = KeyWord +'.txt'
with open(filename, 'w', encoding='utf-8') as f:
    for l in Links:
        f.write(l+"\n")
    f.close()



