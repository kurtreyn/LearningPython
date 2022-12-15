# Selenium Web Scraper
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/kurtreyn/Developer/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("https://python.org")
search_bar = driver.find_element(by="name", value="q")
# print(search_bar.get_attribute("placeholder"))  # returns "Search"

logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")

# print(documentation_link.text)

x_path_docs_link = driver.find_element(By.XPATH, '//*[@id="container"]/li[3]/ul/li[1]/a')

# print(x_path_docs_link.text)


event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for n in range(len(event_times)):
	events[n] = {
		"time": event_times[n].text,
		"name": event_names[n].text
	}

# print(events)

# for time in event_times:
# 	print(time.text)

# for name in event_names:
# 	print(name.text)





# driver.close()  # close down the browser window
driver.quit()  # close down the entire browser











