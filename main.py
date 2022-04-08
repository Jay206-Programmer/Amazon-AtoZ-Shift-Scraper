from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Edge()

driver.get('https://atoz.amazon.work/shifts/dashboard')

driver.find_element(By.ID, "login").send_keys('shuhetal')
driver.find_element(By.ID, "password").send_keys('Ketan@1970')
driver.find_element(By.ID,"buttonLogin").click()

WebDriverWait(driver,100).until(lambda d: d.find_element(By.XPATH, "//input[@value='1']")).click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//input[@value='1']").click()
driver.find_element(By.ID, "buttonContinue").click()

print("\n\nPlease Enter OTP: ")
otp = input()

driver.find_element(By.ID, "code").send_keys(otp)
driver.find_element(By.ID, "buttonVerifyIdentity").click()

time.sleep(6)
driver.find_element(By.CLASS_NAME, "atoz-find-shifts-quicklinks-button").click()



time.sleep(10000)
driver.quit()