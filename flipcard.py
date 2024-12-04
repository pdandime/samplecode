import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(chrome_options)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.title)
print(driver.current_url)
driver.find_element(By.XPATH, "//a[@class='_1jKL3b']").click()
driver.find_element(By.XPATH, "//input[@class='r4vIwl BV+Dqf']").send_keys("8010314806")
driver.find_element(By.XPATH, "//button[@class='QqFHMw twnTnD _7Pd1Fp']").click()
print("welocme to giy")
time.sleep(4)
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "//div[@class='bpjkJb']/span[3]")).perform()
driver.find_element(By.LINK_TEXT,"T-Shirts").click()
driver.find_element(By.XPATH, "//div[@data-id='TSHGQAJAWTFZFRGC']").click()
windowhandl = driver.window_handles
driver.switch_to.window(windowhandl[1])
print("welcome to github")
driver.execute_script("window.scrollBy(0,500)")
driver.find_element(By.XPATH,"//div[@class='_1ri+WN']/ul/li[1]").click()
driver.find_element(By.XPATH, "//div[@class='p2uyH2']/button[2]").click()
driver.refresh()
driver.find_element(By.XPATH, "//button[@class='QqFHMw zA2EfJ _7Pd1Fp']").click()
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("8010314806")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
print("sample")
time.sleep(2)