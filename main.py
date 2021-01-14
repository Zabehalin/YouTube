from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import *
import time

print("start")
myProxy = "192.109.165.41:80"
proxy = Proxy({'proxyType': ProxyType.MANUAL,'httpProxy': myProxy,'ftpProxy': myProxy, 'sslProxy': myProxy,'noProxy':''})
options = Options()
options.headless = False
driver = webdriver.Firefox(options=options, proxy=proxy)
driver.get("https://www.youtube.com/watch?v=UIwhN3hHg7A")
element = driver.find_element_by_class_name("ytp-play-button")
element.click()
time.sleep(15000)
