from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import winsound

driver = webdriver.Edge()
#executable_path="C:\\Users\\kaiki\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python310\\Scripts\\msedgedriver.exe"
time.sleep(2)
driver.get("https://www.bing.com")
time.sleep(15)

search_box = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/form/div[1]/div/textarea")
num=random.randint(0,1000)
search_box.send_keys(num)
time.sleep(1)
search_box.submit()
time.sleep(1)
#URL習得：driver.current_url
k=0
for i in range(33):#6
    search_box = driver.find_element(By.XPATH, "/html/body/header/form/div/textarea")#/html/body/header/form/div/textarea
    num=random.randint(0,1000)
    search_box.send_keys(num)
    time.sleep(1)
    search_box.submit()
    time.sleep(1)
#driver.quit()

time.sleep(10) # Let the user actually see something!
#driver.quit()

driver.get("https://www.bing.com")


winsound.Beep(440,1000)
time.sleep(30)

#playsound.playsound(r"music\sw_on.mp3")
#search_box=driver.find_element(By.XPATH,"/html/body/fluent-design-system-provider/edge-chromium-page//div[5]/cs-header-core/div[2]/common-search-box-edgenext//cs-common-search-box//form/div[1]/input")
#num=random.randint(0,1000)
#search_box.send_keys(num)
#search_box.submit()

for i in range(13):
    search_box = driver.find_element(By.XPATH, "/html/body/header/form/div[1]/textarea")
    num=random.randint(0,1000)
    search_box.send_keys(num)
    time.sleep(1)
    search_box.submit()
    time.sleep(1)
#/html/body/header/form/div/input[1]
#/html/body/header/form/div[1]/textarea
