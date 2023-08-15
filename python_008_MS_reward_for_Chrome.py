import time
import chromedriver_binary
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import playsound
driver = webdriver.Chrome()#'/path/to/chromedriver'  # Optional argument, if not specified will search path.

driver.get('https://www.bing.com/');

#time.sleep(5) # Let the user actually m

search_box = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/form/div[1]/div/textarea")
num=random.randint(0,1000)
search_box.send_keys(num)
time.sleep(1)
search_box.submit()
#!!ここでログイン！！
time.sleep(30)
#playsound.playsound(r"music\sw_on.mp3")
#URL習得：driver.current_url
for i in range(35):
    search_box = driver.find_element(By.XPATH, "/html/body/header/form/div/input[1]")
    num=random.randint(0,1000)
    search_box.send_keys(num)
    time.sleep(1)
    search_box.submit()
    time.sleep(1)
#mailad
#pass
