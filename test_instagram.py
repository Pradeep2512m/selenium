# instagram login

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

username = input("Enter username:")
Password = input("Enter Password:")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.instagram.com/")
driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(Password)
driver.find_element_by_class_name("L3NKy").click()
time.sleep(5)
driver.close()
print("tested succesfully")
