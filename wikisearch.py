import time
import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
url = "https://www.google.com"
driver.get(url)
driver.maximize_window()
wait = WebDriverWait(driver, 5)

# Title verification
current_title = driver.title
if current_title == "google - Google Search":
    print("Current Title is OK: ", driver.title)
else:
    print("Current Title is different than Expected Title", driver.title)
# wait max 5 sec for page load
driver.implicitly_wait(5)

#API testing
code = requests.get(url).status_code
if code == 200:
    print("Url has ", requests.get(url).status_code, " as status Code")
else:
    print("API response code is not 200")

#Search input check
search = driver.find_element(By.NAME,'q')
search.clear()
search.send_keys("Wikipedia")
driver.find_element(By.NAME,'btnK').click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Wikipedia").click()

# Wikipedia Title verification
current_title = driver.title
if current_title == "Wikipedia":
    print("Current Title is OK: ", driver.title)
else:
    print("Current Title is different than Expected Title", driver.title)
# wait max 5 sec for page load
driver.implicitly_wait(5)

#Search input Wikipedia
wiki_search = driver.find_element(By.ID, 'searchInput')
wiki_search.clear()
wiki_search.send_keys("Kazakhstan")

driver.find_element(By.XPATH, '//*[@type="submit"]').click()

# Kazakhstan Title verification
current_title = driver.title
if current_title == "Kazakhstan - Wikipedia":
    print("Current Title is OK: ", driver.title)
else:
    print("Current Title is different than Expected Title", driver.title)

KZ_head = wait.until(EC.visibility_of_element_located((By.ID, 'firstHeading')))
if KZ_head :
    print ("Kazakhstan central logo visible")
else:
    print("Kazakhstan central logo not visible")
wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@class="infobox-above adr"]')))
print ("Inbox KZ logo visible")
flag = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@alt="Flag of Kazakhstan"]')))
if flag:
    print ("Kazakhstan flag is visible")
else:
    print("Kazakhstan flag not visible")
emblem =  wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@alt="Emblem of Kazakhstan"]')))
if emblem:
    print ("Kazakhstan emblem is visible")
else:
    print("Kazakhstan emblem not visible")

Anthem = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@class="infobox-full-data anthem"]')))
if emblem:
    print ("Kazakhstan anthem is visible")
else:
    print("Kazakhstan anthem not visible")

audio = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@class="mw-tmh-play-icon"]')))
if audio:
    print("Audio Anthem plays")
else:
    print("Audio Anthem not playable ")
driver.find_element(By.XPATH,'//*[@href="/wiki/File:Kazakhstan_(orthographic_projection).svg"]').get_attribute("src")
print("Kazakhstan location is visible")

