from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(chrome_options=options, executable_path="C:\Users\Arda\Desktop\chromedriver", )
url = str(input("Hacked Site Url : "))
time.sleep(10)
driver.get("https://mirror-h.org/site-send")
site = driver.find_element_by_name("url")
attacker = driver.find_element_by_name("user")
site.send_keys("" + url + "")
attacker.send_keys("Turkhackteam")
enter = driver.find_element_by_class_name("btn btn-primary mr-2").click()
driver.get("https://mirror-h.org")

