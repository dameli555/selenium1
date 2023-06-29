from selenium import webdriver
from selenium.webdriver.common.by  import By
from faker import Faker
import time

faker_class = Faker()

driver = webdriver.Chrome()
driver.get("https://qasvus.wordpress.com/")
driver.maximize_window()

time.sleep(2)
print(driver.find_element(By.XPATH, '//*[@class="site-title"]//*[text()="California Real Estate"]').get_attribute("href"))

# Webside logo
site_logo = driver.find_element(By.XPATH,'//*[@class="site-logo"]')
if site_logo:
    print("Website logo picture is visiable ")
else:
    print ("Website logo is not visible ")

# Website Menu Button
top_menu = driver.find_element(By.ID,'site-navigation')
if top_menu.is_enabled():
    print(" Button is clickable ")
else:
    print(" Button is not clickable ")

# Small Wix Menu is visible
small_logo = driver.find_element(By.ID, "menu-empty-menu-1")
if small_logo:
    print(" Small logo is visible ")
else:
    print(" Small logo is not visible")

# verify Main Big Picture is visible
maim_pic = driver.find_element(By.XPATH, '//*[@class="wp-block-cover__image-background wp-image-54"]')
if maim_pic.is_displayed:
    print(" Main picture is visible")
else:
    print("Main picture is not visible")

# Main big Text verify is correct
maim_text = driver.find_element(By.ID,'let-s-find-your-dream-home')

actual_text = maim_text.text

expected_text = "Let’s find your dream home."

if actual_text == expected_text:
    print ("Main Text is correct ")
else :
    print("Main Text is not correct ")


#verify Down burger menu is visible
burger_menu = driver.find_element(By.ID, "actionbar")
if burger_menu.is_displayed:
    print("Burger menu is visible")
else:
    print("Burger menu is not visitble")

#verify Down burger menu is clickble
if burger_menu.is_enabled():
    print("Burger menu is clickble")
else :
    print("Burger menu is not clickble")

#scrol down

element = driver.find_element(By.ID, "about-us")
driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(3)

#about us Header

AB_header = driver.find_element(By.ID, "about-us")
if AB_header.is_displayed():
    print("About Us Header  is visible")
else:
    print("About Us Header is not visible")

#small pic #1

small_pic = driver.find_element(By.XPATH, '//*[@class="wp-image-55 size-full"]')
if small_pic.is_displayed():
    print("Small picture #1  is visible")
else:
    print("Small picture #1 is not visible")

text_one = driver.find_element(By.XPATH,"//*[contains(text(), 'No matter the type of home ')]")
actual_text = text_one.text
expected_text = "No matter the type of home you’re in the market for, we’ve got you covered. We’re in your neighborhood– we know what it’s like to live here, too!"

if actual_text == expected_text:
    print ("First Pic Text is correct ")
else :
    print("First Text Text is not correct ")

#scroll #2
element2 = driver.find_element(By.XPATH, '//*[@class="wp-image-34 size-full"]')
driver.execute_script("arguments[0].scrollIntoView();", element2)
time.sleep(3)

# pic #2
small_pic = driver.find_element(By.XPATH, '//*[@class="wp-image-34 size-full"]')
if small_pic.is_displayed():
    print("Small picture #2  is visible")
else:
    print("Small picture #2 is not visible")

text_one = driver.find_element(By.XPATH,"//*[contains(text(), 'Build lasting memories')]")
actual_text = text_one.text
expected_text = "Build lasting memories for years to come. We’ll help you find the perfect home  without breaking the bank."

if actual_text == expected_text:
    print ("Second Pic Text is correct ")
else :
    print("Second Text Text is not correct ")

#scroll to our services
element3 = driver.find_element(By.ID, 'our-services')
driver.execute_script("arguments[0].scrollIntoView();", element3)
time.sleep(3)

# Our services

services = driver.find_element(By.ID, 'our-services')
if services.is_displayed():
    print("Services Header is visiable ")
else :
    print("Services Header is not visiable ")

# pic #3
print(driver.find_element(By.XPATH,'//*[@class="wp-image-56 size-full"]').get_attribute("src"))

interior = driver.find_element(By.ID, 'interior-decorating')
if interior.is_displayed():
    print("interior-decorating is visible ")
else:
    print("interior-decorating is not visible ")

text_third  = driver.find_element(By.XPATH,"//*[contains(text(), 'We’ll work closely with')]")
actual_text = text_third.text
expected_text = "We’ll work closely with you to transform your home into something that reflects your personality (and your budget)."

if actual_text == expected_text:
    print ("Third Pic Text is correct ")
else :
    print("Third Text Text is not correct ")

#scroll to our services # 4
element4 = driver.find_element(By.XPATH,'//*[@class="wp-image-30 size-full"]')
driver.execute_script("arguments[0].scrollIntoView();", element4)
time.sleep(3)

# pic #4
print(driver.find_element(By.XPATH,'//*[@class="wp-image-30 size-full"]').get_attribute("src"))

interior = driver.find_element(By.ID, 'remodeling')
if interior.is_displayed():
    print("remodeling header is visible ")
else:
    print("remodeling header is not visible ")

text_four  = driver.find_element(By.XPATH,"//*[contains(text(), 'Thinking about making ')]")
actual_text = text_four.text
expected_text = "Thinking about making some renovations? Our team of experienced architects can help you draft a plan."

if actual_text == expected_text:
    print ("Four Pic Text is correct ")
else :
    print("Four Text Text is not correct ")

#scroll to Get in Touch
element_get = driver.find_element(By.ID,'get-in-touch')
driver.execute_script("arguments[0].scrollIntoView();", element_get)
time.sleep(3)

touch_Header = driver.find_element(By.ID, "get-in-touch")
if touch_Header.is_displayed():
    print("Get in Touch header is visible ")
else :
    print("Get in Touch header is not visible ")


real_estate = driver.find_element(By.XPATH,"//strong[contains(text(),'California Real Estate')]")
if real_estate:
    print("Real Estate Header is on page ")
else :
    print("Real Estate Header is not  on page ")

estate_address = driver.find_element(By.XPATH, "//*[contains(text(),'123 Main St')] ")
actual_text = estate_address.text
expected_text = "123 Main St, 555-555-5555"
if actual_text == expected_text :
    print("Address is correct : 123 Main St ")
else:
    print("Address is not correct ")

#scroll to Send Us Message
element_get = driver.find_element(By.ID,'send-us-a-message')
driver.execute_script("arguments[0].scrollIntoView();", element_get)
time.sleep(3)

message = driver.find_element(By.ID, 'send-us-a-message')
if message.is_displayed():
    print("Send Us a Message Header is visible")
else:
    print("Send Us a Message Header is not  visible")

# Name input
name = driver.find_element(By.XPATH,'//*[@for="g2-name"]')
if name.is_displayed():
    print("Name input is visible")
else:
    print("Name input is not  visible")

type_name = driver.find_element(By.ID, 'g2-name')
type_name.click()
type_name.send_keys(faker_class.name())
print("Generated Name:", name)

time.sleep(2)

# Email input
email = driver.find_element(By.XPATH,'//*[@for="g2-email"]')
if email.is_displayed():
    print("Email input is visible")
else:
    print("Email input is not  visible")

type_email = driver.find_element(By.ID, 'g2-email')
type_email.click()
type_email.send_keys(faker_class.email())
print("Generated Email :", email)

time.sleep(2)

# Message input
message2 = driver.find_element(By.XPATH,'//*[@for="contact-form-comment-g2-message"]')
if message2.is_displayed():
    print("Message input is visible")
else:
    print("Message input is not  visible")

type_message2 = driver.find_element(By.ID, 'contact-form-comment-g2-message')
type_message2.click()
type_message2.send_keys(faker_class.text())


time.sleep(1)

driver.find_element(By.XPATH, '//*[@class="pushbutton-wide"]').click()
time.sleep(2)
driver.quit()



