from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time

# Path for chrome driver
chromeDriverpath = "./chromedriver"

driver = webdriver.Chrome(chromeDriverpath)
driver.get("https://web.whatsapp.com/")

print("Scan the QR code using your phone and press enter when the whatsapp loads")
input()

# The icons status, new chat and options 
headElements = driver.find_elements_by_class_name("PVMjB")

# Chat element
newChatElement = headElements[1]

actions = ActionChains(driver)

# Clicking the new chat element using ActionsChains
actions.move_to_element(newChatElement).click(newChatElement).perform()

# To wait until the page loads in order to avoid any errors
time.sleep(2)

# Text Area where we search for contacts
search_area = driver.find_element_by_class_name("_3FRCZ")
receipientName = input("Enter the name of the person with whom you want to chat(Exactly as you saved in your phone): ")
search_area.send_keys(receipientName)

time.sleep(60)
try:
    resultChatElement = driver.find_element_by_class_name("_2kHpK")
except:
    driver.quit()
    exit()

# Clicking the chat
webdriver.ActionChains(driver).move_to_element(resultChatElement).click(resultChatElement).perform()


# At all places whatsapp has made same css classes for all search elements.
chatMessage = input("Enter the message which you want to send: ")

numberOfMessages = int(input("Enter the number of times you want to send this message(Recommended less than 30): "))

confirmMessage = input("Are you sure(Yes/No): ")


if confirmMessage == "No":
    print("Thank you for using.")
    driver.quit()
    exit()

else:
# Two search fields, both having same class name. The second is the one where we type or chat  
    textAreas = driver.find_elements_by_class_name("_3FRCZ")

    actualChatArea = textAreas[1]

    for i in range(numberOfMessages+30):
        actions = ActionChains(driver)
        actions.move_to_element(actualChatArea).click(actualChatArea).perform()
        actualChatArea.send_keys(chatMessage)
        submitButton = driver.find_element_by_class_name("_1U1xa")
        actions.move_to_element(submitButton).click(submitButton).perform()

# To wait until all the messages are sent
time.sleep(10)

print("Your successfully spammed your friend!+30 then u wished")
driver.quit()
