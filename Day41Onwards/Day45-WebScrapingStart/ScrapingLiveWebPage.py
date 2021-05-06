from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/news")
webpage = response.text

soup = BeautifulSoup(webpage,"html.parser")
article_texts = []
article_links = []

articles_tags = soup.find_all(name="a",class_="storylink")

for article_tag in articles_tags:
    Title = article_tag.getText()
    article_texts.append(Title)
    Link = article_tag.get("href")
    article_links.append(Link)


articelUpvote = [int(item.getText().split(" ")[0]) for item in  soup.find_all(name="span",class_="score")]
highest_voted = max(articelUpvote)
index_highest_voted = articelUpvote.index(highest_voted)
print("Hackernews Article with Highest Upvotes Today ⬇⬇⬇⬇⬇")
print(article_texts[index_highest_voted])
print(article_links[index_highest_voted])