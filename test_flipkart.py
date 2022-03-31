from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
product = input("Enter the product to searched :")
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(ChromeDriverManager().install())
print("Testcase started")

driver.maximize_window()
driver.get("https://www.flipkart.com/")
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
driver.find_element_by_name("q").send_keys(product)
driver.find_element_by_class_name("LOZ3Pu").send_keys(Keys.ENTER)
time.sleep(5)
driver.close()
print("testcase completed")