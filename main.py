from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")
story_tag = soup.find_all(name="a", class_="titlelink")
story_title = []
story_link = []
for tag in story_tag:
    title = tag.getText()
    story_title.append(title)
    link = tag.get("href")
    story_link.append(link)

story_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_upvote = max(story_upvote)
index = story_upvote.index(max_upvote)
print(story_upvote[index])
print(story_title[index])
print(story_link[index])
















































# import lxml
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# #print(soup.title.name)
# #print(soup.title.string)
# #print(soup.prettify())
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# # heading = soup.find(name="h1", id="name")
# # print(heading)
# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading)
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# headings = soup.select_one(selector="#name")
# print(headings)
#
# headings = soup.select(selector=".heading")
# print(headings)