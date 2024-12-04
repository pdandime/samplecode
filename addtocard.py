import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/auth/login")
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.title)
print(driver.current_url)
driver.find_element(By.ID, 'firstName').send_keys("preeti")
driver.find_element(By.ID,'lastName').send_keys("dandime")
driver.find_element(By.ID,'userEmail').send_keys("preetidandime72@gmail.com")
driver.find_element(By.ID, 'userMobil').send_keys("8010314806")
dropdown = Select(driver.find_element(By.XPATH," //select[@class='custom-select ng-pristine ng-valid ng-touched']"))
dropdown.deselect_by_visible_text("3: Engineer")
driver.find_element(By.XPATH, "//input[@value='Female']").click()
driver.find_element(By.ID, 'userPassword').send_keys("8010314806")
driver.find_element(By.ID, 'confirmPassword').send_keys("8010314806")
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
driver.find_element(By.ID,'login').click()
