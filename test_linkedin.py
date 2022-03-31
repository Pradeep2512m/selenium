from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(ChromeDriverManager().install())
print("Testcase started")

driver.maximize_window()
driver.get("https://www.LinkedIn.com/")
driver.find_element_by_name("session_key").send_keys("pradeep2512m@gmail.com")
time.sleep(2)
driver.find_element_by_name("session_password").send_keys("rude_radee")
time.sleep(2)
driver.find_element_by_name("loginFlow").send_keys(Keys.ENTER)
time.sleep(10)
driver.close()
print("testcase completed")
