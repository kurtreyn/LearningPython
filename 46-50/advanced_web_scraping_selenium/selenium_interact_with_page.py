from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/kurtreyn/Developer/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)
# article_count.click()

contents_link = driver.find_element(By.LINK_TEXT, "Contents")
# contents_link.click()

search = driver.find_element(By.NAME, "search")
# print(search)
search.send_keys("Python")
search.send_keys(Keys.ENTER)






driver.quit()  # close down the entire browser