from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
driver.get("www.gmail.com")

driver.maximize_window()
print(driver.title)