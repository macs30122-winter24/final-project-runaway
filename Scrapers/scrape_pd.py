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

# Note that, due to the ugly naming style of this website
#our codes can exist 80 char per row standard, which is unevitable, sorry.

def ScrapePost(ID):
    # Start Chrome and get to the website 
    browser = webdriver.Chrome(executable_path="/Users/jingzhixu/Parking Lot/MACSS/2024winter/30122/chromedriver")
    browser.get("http://lihkg.com/thread/"+ID)
    problem = False
    timeout = 100
    colnames = ["time","text","support","against"]
    result = dict.fromkeys(colnames, None)
    result["post_id"] = ID
    try:
        element_text = EC.presence_of_element_located((By.CLASS_NAME, '_36ZEkSvpdj_igmog0nluzh'))
        WebDriverWait(browser, timeout).until(element_text)
    except TimeoutException:
        print ("Timed out waiting for page to load" )
        problem = True
    
    if (not problem):
        content = browser.find_element_by_class_name('_1H7LRkyaZfWThykmNIYwpH')
        opt = content.find_elements_by_tag_name('option') 
        L = len(opt)
        for counter in range(L):
            time.sleep(random.randint(5,10))
            browser.get("http://lihkg.com/thread/"+ID+"/page/"+str(counter+1))
            timeout = 100
            try:
                element_present = EC.presence_of_element_located((By.CLASS_NAME, '_36ZEkSvpdj_igmog0nluzh'))
                WebDriverWait(browser, timeout).until(element_present)
          
            except TimeoutException:
                problem = True
                
            if(not problem): 
                content = browser.find_elements_by_class_name('_36ZEkSvpdj_igmog0nluzh')
                opt = content.find_elements_by_tag_name('option') 
                i = len(opt)
                for counter in range(1, i):
                    time.sleep(random.randint(5,10))
                    browser.get("http://lihkg.com/thread/"+ID+"/page/"+str(counter)) #navigate to the page by page no
                    timeout = 15
                    
                    try:
                        element_present = EC.presence_of_element_located((By.CLASS_NAME, '_36ZEkSvpdj_igmog0nluzh'))
                        WebDriverWait(browser, timeout).until(element_present)
                    except TimeoutException:
                        problem = True
                    if(not problem):
                        time.sleep(random.randint(5,10))
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
                date = r['time']
                yearM = []
                for i in date:
                    ym  = re.findall(r"\d{4}\w\d+",i)
                    yearM.append(re.split(r"年", ym[0]))
                r["year"] = [i[0] for i in yearM]
                r["month"] = [i[1] for i in yearM]
    if (browser!=None):
        browser.quit()  
    
    return r
                
                
# Try      

test_id = '3573503'    
rr = ScrapePost(test_id)
rr.to_csv("sampleOutput3573503.csv", index=False)					

    
       
    
    
