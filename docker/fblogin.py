from selenium import webdriver
from selenium.webdriver.chrome.service import Service
browser = webdriver.Chrome(executable_path="chromedriver")

driver = browser.get("https://www.facebook.com")

FB_URL = "https://fb.com"

txtUser = browser.find_element_by_id("email")
txtUser.send_keys("thangnch") # <---  Điền username thật của các bạn vào đây

txtPass = browser.find_element_by_id("pass")
txtPass.send_keys("passwordfake")

sleep(5)

browser.close()


class FacebookLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
 
    def login(self):
        pass
 
    def verify_login(self):
        pass
    
    
def random_sleep(min_s, max_s):
    sleep(randint(min_s, max_s))
