
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
#api testing

# Title verification
current_title = driver.title
if current_title == "Wikipedia":
    print("Current Title is OK: ", driver.title)
else:
    print("Current Title is different than Expected Title", driver.title)
# wait max 5 sec for page load
driver.implicitly_wait(5)
# verify Google logo
print(driver.find_element(By.XPATH, '//*[@class="lnXdpd"]').get_attribute("src"))
# this command find search batten and enter Wikipedia
driver.find_element(By.NAME, "q").send_keys("Wikipedia")
driver.find_element(By.NAME, "btnK").click()
driver.implicitly_wait(5)
# this command go into Wikipedia webpage
driver.find_element(By.XPATH, "//h3[contains(text(),'Wikipedia')]").click()
#driver.find_element(By.XPATH, '//*[@xpath="1"]').click()
driver.implicitly_wait(5)
# checking visibility of element central logo
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="central-textlogo"]')))
print ("Wikipedia central logo visible")
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="central-featured"]')))
print("Wikipedia globus is visible")
# this command check clickable of element central logo
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'English')))
print("English butten is clickable")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'日本語')))
print("日本語 butten is clickable")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'Русский')))
print("Русский butten is clickable")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'Français')))
print("Français butten is clickable")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'Deutsch')))
print("Deutsch butten is clickable")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'Español')))
print("Español butten is clickable")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'Italiano')))
print("Italiano butten is clickable")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'中文')))
print("中文 butten is clickable")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'فارسی')))
print("فارسی butten is cliclble")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'Português')))
print("Português butten is clickable")
# check search battens is clickable
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "searchInput")))
print("Search bar butten is clickable")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@type="submit"]')))
print("Search butten is clickable")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'jsLangLabel')))
print("Search Language butten is clickable")
# check if Search line is functional
search = driver.find_element(By.ID, "searchInput")
if search :
    print("Search line is on page")
else:
    print("Search line is not on page ")
drop_down = Select(driver.find_element(By.ID, 'searchLanguage'))
#drop_down.select_by_visible_text("Қазақша / Qazaqşa / قازاقشا")
options = drop_down.options
for option in options:
    print(option.text)
search_submit = driver.find_element(By.XPATH, '//*[@type="submit"]')
if search_submit.is_enabled():
    print(" Search submit batten is clickable")
else:
    print("Search Submit batten not clickable")
# read wikipedia in your languages drop down is visible
languages = driver.find_element(By.ID, 'js-lang-list-button')
languages.click()
wait.until(EC.visibility_of_element_located((By.ID, 'js-lang-lists')))
print("Languages list is visible")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@data-jsl10n="other-languages-label"]')))
print("Other Languages butten is cliclble")
#scroll page down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# check visibility of down page logos
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="footer"]')))
print ("Footer is visible")
#Assret if Support and donation text is correct
x = driver.find_element(By.XPATH,'//*[@class="footer-sidebar-text jsl10n"]').text
print (x)
assert x == 'Wikipedia is hosted by the Wikimedia Foundation, a non-profit organization that also hosts a range of other projects.'
time.sleep(3)
link = driver.find_element(By.XPATH, '//*[@data-jsl10n="footer-donate"]').get_attribute('href')
print(link)

download = driver.find_element(By.XPATH, '//*[@data-jsl10n="portal.app-links.url"]').get_attribute("href")
download_text = driver.find_element(By.XPATH, '//*[@data-jsl10n="portal.app-links.description"]').text
print(download_text)

# Google pay link testing
"""
def test_link_works():
    try:
        r = requests.get("https://play.google.com/store/apps/details?id=org.wikipedia&referrer=utm_source%3Dportal%26utm_medium%3Dbutton%26anid%3Dadmob")
        assert r.status_code == 200, "Link is broken"
        driver.get("https://play.google.com/store/apps/details?id=org.wikipedia&referrer=utm_source%3Dportal%26utm_medium%3Dbutton%26anid%3Dadmob")
        link = driver.find_element(By.XPATH,"//a[@href='https://play.google.com/store/apps/details?id=org.wikipedia&referrer=utm_source%3Dportal%26utm_medium%3Dbutton%26anid%3Dadmob']")
        link.click()
        assert driver.current_url == "https://play.google.com/store/apps/details?id=org.wikipedia&referrer=utm_source%3Dportal%26utm_medium%3Dbutton%26anid%3Dadmob", "Link is broken"
        time.sleep(5)
    finally:
        driver.quit()
        """

link_GooglePlay = "https://play.google.com/store/apps/details?id=org.wikipedia&referrer=utm_source%3Dportal%26utm_medium%3Dbutton%26anid%3Dadmob"

response = requests.get(link_GooglePlay)

if response.status_code == 200:
    print("Google link works!")
else:
    print("Google link is broken!")

link_appStore = "https://itunes.apple.com/app/apple-store/id324715238?pt=208305&ct=portal&mt=8"

response = requests.get(link_appStore)

if response.status_code == 200:
    print("App Store link is works")
else:
    print("App Store link not works")

# Other projects Wikipedia links check
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Commons")))
print("Common Other project is clickable")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Wikivoyage")))
print("Wikivoyage Other project is clickable")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Wiktionary")))
print("Wiktionary Other project is clickable")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Wikibooks")))
print("Wikibooks Other project is clickable")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Wikinews")))
print("Wikinews Other project is clickable")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Wikidata")))
print("Wikidata Other project is clickable")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Wikiversity")))
print("Wikiversity Other project is clickable")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Wikiquote")))
print("Wikiquote Other project is clickable")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"MediaWiki")))
print("MediaWiki Other project is clickable")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Wikisource")))
print("Wikisource Other project is clickable")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Wikispecies")))
print("Wikispecies Other project is clickable")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Meta-Wiki")))
print("Meta-Wiki Other project is clickable")
driver.quit()
