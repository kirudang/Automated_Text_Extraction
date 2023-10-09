from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# Load the website
web = webdriver.Chrome()
web.get('https://secure.sonnet.ca/#/quoting/property/about_you?lang=en')

# Wating for the web to load before filling out
time.sleep(5)

# Inputs field
#ADDRESS
Address_input = "50 Laughton Ave M6N 2W9" # KEY
Address_fill = web.find_element("xpath",'//*[@id="addressInput"]')
Address_fill.send_keys(Address_input)

# FIRST NAME
FirstName_input = "Kiel" # KEY
FirstName_fill = web.find_element("xpath",'//*[@id="firstName"]')
FirstName_fill.send_keys(FirstName_input)

# LAST NAME
LastName_input = "Dang" # KEY
LastName_fill = web.find_element("xpath",'//*[@id="lastName"]')
LastName_fill.send_keys(LastName_input)

# MONTH OF BIRTH
dropdown_month = web.find_element("id","month-0Button")
dropdown_month.click()
option = web.find_element("xpath", "//span[contains(text(), 'January')]") #KEY
option.click()

# DATE OF BIRTH
Date_input = "23" # KEY
Date_fill = web.find_element("xpath",'//*[@id="date-0"]')
Date_fill.send_keys(Date_input)

# YEAR OF BIRTH
Year_input = "1994" # KEY
Year_fill = web.find_element("xpath",'//*[@id="year-0"]')
Year_fill.send_keys(Year_input)

# Prevent auto closing the web after application finishes the script.
input("Press enter to close the browser")
web.quit()

