from selenium import webdriver
from selenium.webdriver.chrome.service import Service
browser = webdriver.Chrome(executable_path="chromedriver")

driver = browser.get("https://www.facebook.com")
print(driver.title)
sleep(5)

browser.close()