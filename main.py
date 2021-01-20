from threading import Thread
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

print("starting...")

def main():


	options = Options()
	options.headless = False
	driver = webdriver.Firefox(options=options)
	driver.get("https://duckduckgo.com")
	search = driver.find_element_by_id("search_form_input_homepage")
	search.send_keys("Dubno Ukraine July 1992")
	search_btn = driver.find_element_by_id("search_button_homepage").click()
	videos = driver.find_element_by_class_name("js-zci-link--videos").click()
	name = driver.find_element_by_css_selector("div.tile--c--w:nth-child(3) > div:nth-child(1) > img:nth-child(1)").click()
	watch = driver.find_element_by_class_name("overlay__btn").click()
#
def threads():
	for item in range(10):
		thread = Thread(target=main)
		thread.start()

if __name__ == "__main__":
	threads()
