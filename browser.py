import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
print("abc")
print("xyz")
driver.find_element(By.LINK_TEXT, "Today's Deals").click()
#driver.find_element(By.XPATH, "//a[@href='/deals?ref_=nav_cs_gb'']").click()
#driver.find_element(By.LINK_TEXT, "Mobiles").click()
options = driver.find_elements(By.XPATH, "(//div[@class='a-carousel-viewport'])[2]/ol/li")
print(len(options))
for option in options:
    print(option.text)
    time.sleep(5)
    option.find_element(By.XPATH, "(//div[@class='a-carousel-viewport'])[2]/ol/li[3]").click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//div[@data-testid='virtuoso-item-list']//p").click()
#mobile.find_element(By.XPATH, "//div[@data-testid='B0CZS3B3PY']").click()
time.sleep(5)
#service_obj = Service("C:\\Users\\Krushna\\eclipse-workspace\\practice2\\target\\classes\\driver\\chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)
#driver.get("https://www.google.com")