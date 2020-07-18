from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

def  windowhandling():
    driver.get("https://www.google.com/")
    print(driver.title)
    driver.find_element(By.PARTIAL_LINK_TEXT,"Gmail").click()
    driver.maximize_window()
    print(driver.title)
    time.sleep(3)
    driver.find_element(By.PARTIAL_LINK_TEXT,"Create an account").click()
    time.sleep(3)
    driver.maximize_window()
    windowHandles=driver.window_handles
    i=0
    for Handle in windowHandles:
        print ("value of window ", i, "is:", Handle)
        i=i+1
    print(driver.title)
    driver.switch_to.window(Handle)
    print("Header of create account page is: ", driver.find_element(By.XPATH,"//h1[contains(text(),'Create your Google Account')]").is_displayed())
    print( driver.find_element(By.XPATH,"//h1[contains(text(),'Create your Google Account')]").text)
    driver.quit()
windowhandling()

def scrollHandling():
    driver.get("https://www.ebay.com/")
    driver.maximize_window()
    driver.execute_script("window.scrollBy(0,900)",'')
    time.sleep(5)
    ele=driver.find_element(By.XPATH,"//a[@id='gf-fbtn']")
    driver.execute_script("arguments[0].scrollIntoView();",ele)
    time.sleep(5)
    ele=driver.find_element(By.XPATH,"//a[contains(text(),'Popular Destinations')]")
    driver.execute_script("arguments[0].scrollIntoView();",ele)
    time.sleep(5)
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
scrollHandling()
driver.close()

def webTableonMouseHoverAndClick():
    driver.get("https://opensource-demo.orangehrmlive.com")
    driver.maximize_window()
    driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys("admin")
    driver.find_element(By.XPATH,"//input[@id='txtPassword']").send_keys("admin123")
    driver.find_element(By.ID,"btnLogin").click()
    time.sleep(5)
    eleLnkAdmin=driver.find_element(By.XPATH,"//a[@id='menu_admin_viewAdminModule']")
    eleUserManagement=driver.find_element(By.XPATH,"//a[@id='menu_admin_UserManagement']")
    eleUsers=driver.find_element(By.XPATH,"//a[@id='menu_admin_viewSystemUsers']")
    Actions=ActionChains(driver)
    Actions.move_to_element(eleLnkAdmin).move_to_element(eleUserManagement).move_to_element(eleUsers).click().perform()
    time.sleep(5)
webTableonMouseHoverAndClick()
