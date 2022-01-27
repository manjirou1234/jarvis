from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

path = ChromeDriverManager().install()
s = Service(path)

def open_google_and_search():
    text = "kiếm NaOH tác dụng với HCl"
    search_for = text.split("kiếm", 1)[1]
    driver = webdriver.Chrome(service=s)
    driver.get("http://www.google.com")
    que = driver.find_element_by_name("q")
    que.send_keys(str(search_for))
    que.send_keys(Keys.RETURN)

open_google_and_search()