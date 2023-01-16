
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")
driver.maximize_window()
wait = WebDriverWait(driver, 5)


# verify Wikipedia for clickble and visibles
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="central-featured"]')))
print(" center logo is visible")
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="central-textlogo"]')))
print(" wikipedia header is visible")
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="footer"]')))
print(" footer is visible")
wait.until(EC.visibility_of_element_located((By.ID, 'searchInput')))
print(" search is visible")

corgi_search = driver.find_element(By.ID, 'searchInput') #searching using variables
corgi_search.clear()
corgi_search.send_keys("Welsh Corgi")
corgi_search.submit()

wait.until(EC.visibility_of_element_located((By.ID, "firstHeading")))  #verify logos is visible
#wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "infobox biota")))
wait.until(EC.visibility_of_element_located((By.ID, "mw-head")))
wait.until(EC.visibility_of_element_located((By.ID, "mw-panel")))

driver.find_element(By.XPATH, '//*[@alt="Welchcorgipembroke.JPG"]').click() #check all images
time.sleep(2)
driver.find_element(By.CLASS_NAME, "mw-mmv-next-image").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "mw-mmv-next-image").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "mw-mmv-next-image").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "mw-mmv-next-image").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "mw-mmv-next-image").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "mw-mmv-close").click()

driver.find_element(By.CLASS_NAME, "mw-wiki-logo").click()
driver.quit()





