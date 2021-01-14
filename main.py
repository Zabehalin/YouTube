from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

print("start")

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get("https://www.youtube.com/watch?v=UIwhN3hHg7A")
element = driver.find_element_by_class_name("ytp-play-button")
element.click()
