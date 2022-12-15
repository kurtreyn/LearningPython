from bs4 import BeautifulSoup
# import lxml

with open("website.html") as file:
	contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
title = soup.title
a_tag = soup.a
# print(soup.prettify())
# print(title.string)
# print(a_tag)

all_anchor_tags = soup.find_all(name="a")
all_paragraph_tags = soup.find_all(name="p")
# print(all_anchor_tags)
# print(all_paragraph_tags)

# for tag in all_anchor_tags:
	# print(tag.getText())
	# print(tag.get("href"))

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

company_url = soup.select_one(selector="p a")
name = soup.select_one("#name")
headings = soup.select(".heading")
# print(company_url)
# print(name)
# print(headings)