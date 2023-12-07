#YOU NEED GOOGLE CHROME INSTALLED
#YOU NEED PYTHON INSTALLED
#YOU NEED SELENIUM LIB INSTALLED
#YOU NEED SELENIUM WEBDRIVER-MANAGER LIB INSTALLED


#IMPORT ALL SELENIUM LIBS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#IMPORT TIME LIB
import time
#PUT YOUR LOGIN INFO HERE, SO THE BOT CAN LOG INTO THE ACCOUNT
emailVAR = "INSERT YOUR EMAIL HERE"
passVAR = "INSERT YOUR PASSWORD HERE"
#GET THE PROFILE @ SO THE BOT CAN FOLLOW IT
print("WHICH PROFILE DO YOU WANNA FOLLOW?")
profile = input("@")
#TURN THE PROFILE INTO A LINK
profile_link = (f"https://www.instagram.com/{profile}/")
#OPEN THE BROWSER
driver = webdriver.Chrome()
#OPEN THE INSTAGRAM
driver.get("https://www.instagram.com/")
#WAIT 3 SECONDS
time.sleep(3)
#GET THE EMAIL, PASSWORD AND LOGIN BUTTON SO THE BOT CAN CLICK IT
email = driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')

password = driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')

loginbutton = driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button/div')
#WAIT HALF A SECOND
time.sleep(0.5)
#PUT THE LOGIN INFO INTO THE INPUT SECTION
email.send_keys(emailVAR)
time.sleep(1)
password.send_keys(passVAR)
#WAIT A COUPLE SECONDS
time.sleep(1.5)
#CLICK THE LOGIN BUTTON
loginbutton.click()
#WAIT A COUPLE SECONDS UNTIL THE PAGE LOADS
time.sleep(7)
#GO TO THE PROFILE LINK
driver.get(profile_link)
#WAIT A COUPLE SECONDS UNTIL THE PAGES LOAD
time.sleep(6)
#GET THE FOLLOW BUTTON
follow = driver.find_element(by=By.CSS_SELECTOR, value='.\_aacw')
#CLICK IN IT
follow.click()
#WELL DONE!
time.sleep(10)
