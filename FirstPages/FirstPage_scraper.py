from selenium import webdriver

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import re
import random
import pandas as pd
import csv
import sys
# Note that, due to the ugly naming style of this website
#our codes can exist 80 char per row standard, which is unevitable, sorry.

# In this version we scroll pages that arrange post in order of score
#and only include the first page.

def ScrapePost(ID):
    colnames = ["time","text","support","against"]
    result = dict.fromkeys(colnames, None)
    result["post_id"] = ID
    
    # Start Chrome and get to the website 
    browser = webdriver.Chrome(executable_path="/Users/jingzhixu/Parking Lot/MACSS/2024winter/30122/chromedriver")
    browser.get("http://lihkg.com/thread/"+ID+"/page/1?order=score")
    problem = False
    timeout = 300
    try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, '_36ZEkSvpdj_igmog0nluzh'))
        WebDriverWait(browser, timeout).until(element_present)
    except TimeoutException:
        print ("Timed out waiting for page to load" )
        problem = True
    if (not problem):        
        print("Scraping starts! Now we're scraping post " + ID)                
        content = browser.find_elements_by_class_name('_36ZEkSvpdj_igmog0nluzh')
        Time = browser.find_elements_by_class_name('Ahi80YgykKo22njTSCzs_')
        for cont in content:
            if re.search(r'\n\d+\n\d+$', cont.text):
                sepCont = re.split(r"\n", cont.text)
                if result['text'] == None:
                    result['text'] = [sepCont[4:-2]]
                else:
                    result['text'].append(sepCont[4:-2])
                    
                if result['support'] == None:
                    result['support'] = [sepCont[-2]]
                else:
                    result['support'].append(sepCont[-2])
                    
                if result['against'] == None:
                    result['against'] = [sepCont[-1]]
                else:
                    result['against'].append(sepCont[-1])
        for t in Time:
            if result['time'] == None:
                result['time'] = [t.get_attribute('title')]
            else:
                result['time'].append(t.get_attribute('title'))
        if result['time'] != None:
            L = min(len(result['time']),len(result['text']))
            result['time'] = result['time'][0:L-1]
            result['text'] = result['text'][0:L-1]
            result['support'] = result['support'][0:L-1]
            result['against'] = result['against'][0:L-1]
        
            r = pd.DataFrame(result)
            date = result['time']
            yearM = []
            for i in date:
                ym  = re.findall(r"\d{4}\w\d+",i)
                yearM.append(re.split(r"年", ym[0]))
            r["year"] = [i[0] for i in yearM]
            r["month"] = [i[1] for i in yearM]
        else:
            r = None
    if (browser!=None):
        print("Scraping finished!")
        browser.quit()  
    
    return r
# Get ids
with open('./Post_id/民主ids.txt', 'r') as file:
    ids = file.read()

IDs = re.split(r"\n", ids)

with open('./Post_id/公义ids.txt', 'r') as file:
    ids = file.read()

IDs.extend(re.split(r"\n", ids))

with open('./Post_id/保衛ids.txt', 'r') as file:
    ids = file.read()

IDs.extend(re.split(r"\n", ids))

with open('./Post_id/普選ids.txt', 'r') as file:
    ids = file.read()

IDs.extend(re.split(r"\n", ids))


R = ScrapePost(IDs[0])
for i in range(1,len(IDs)):
    print(i)
    print("*********************")
    r = ScrapePost(IDs[i])
    R = pd.concat([R, r], ignore_index=True)
    print(R.tail())
    time.sleep(random.randint(5,10))


R.to_csv("demoJust.csv")
