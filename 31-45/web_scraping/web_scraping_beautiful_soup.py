from bs4 import BeautifulSoup
import lxml
import requests

# with open("website.html") as file:
# 	contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# title = soup.title
# a_tag = soup.a
# print(soup.prettify())
# print(title.string)
# print(a_tag)

# all_anchor_tags = soup.find_all(name="a")
# all_paragraph_tags = soup.find_all(name="p")
# print(all_anchor_tags)
# print(all_paragraph_tags)

# for tag in all_anchor_tags:
# print(tag.getText())
# print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# company_url = soup.select_one(selector="p a")
# name = soup.select_one("#name")
# headings = soup.select(".heading")
# print(company_url)
# print(name)
# print(headings)


# -------------------- SCRAPING A LIVE WEBSITE --------------

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []

for article_tag in articles:
	text = article_tag.getText()
	article_texts.append(text)
	link = article_tag.get("href")
	article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
# print(article_texts)
print(article_texts[largest_index])
print(article_links[largest_index])
