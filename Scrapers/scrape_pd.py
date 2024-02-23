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

def ScrapePost(ID):
    colnames = ["time","text","support","against"]
    result = dict.fromkeys(colnames, None)
    result["post_id"] = ID
    
    # Start Chrome and get to the website 
    browser = webdriver.Chrome(executable_path="/Users/jingzhixu/Parking Lot/MACSS/2024winter/30122/chromedriver")
    browser.get("http://lihkg.com/thread/"+ID)
    problem = False
    timeout = 100
    try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, '_36ZEkSvpdj_igmog0nluzh'))
        WebDriverWait(browser, timeout).until(element_present)
    except TimeoutException:
        print ("Timed out waiting for page to load" )
        problem = True
    if (not problem):
        content = browser.find_element_by_class_name('_1H7LRkyaZfWThykmNIYwpH')
        opt = content.find_elements_by_tag_name('option') 
        L = len(opt)
        print("Scraping starts! Now we're scraping post " + ID)
        for counter in range(20,L):
            browser.get("http://lihkg.com/thread/"+ID+"/page/"+str(counter+1))
            time.sleep(random.randint(5,10))
            try:
                element_present = EC.presence_of_element_located((By.CLASS_NAME, '_36ZEkSvpdj_igmog0nluzh'))
                WebDriverWait(browser, timeout).until(element_present)
          
            except TimeoutException:
                problem = True
                
            if(not problem):  
                print("We're now on page" + str(counter))
                time.sleep(random.randint(2,5))
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

            r = pd.DataFrame(result)
            date = result['time']
            yearM = []
            for i in date:
                ym  = re.findall(r"\d{4}\w\d+",i)
                yearM.append(re.split(r"年", ym[0]))
            r["year"] = [i[0] for i in yearM]
            r["month"] = [i[1] for i in yearM]
    if (browser!=None):
        print("Scraping finished!")
        browser.quit()  
    
    return r
                
                
# Try      

test_id = '3573503'    
rr = ScrapePost(test_id)
rr.to_csv("sampleOutput3573503.csv", index=False)					

# Try merge together

rrr = pd.concat([rr, rr], ignore_index=True)

# Run iteratively for all posts under a key word
with open('./Post_id/民主ids.txt', 'r') as file:
    ids = file.read()

IDs = re.split(r"\n", ids)
R = ScrapePost(IDs[0])
t = 9
for i in range(t,len(IDs)):
    print(i)
    print("*********************")
    r = ScrapePost(IDs[i])
    R = pd.concat([R, r], ignore_index=True)
    print(R.tail())
    time.sleep(random.randint(40,60))
    t += 1
 
R.to_csv('Democracy.csv', index=False)   
    