from bs4 import BeautifulSoup
import requests


website_url = "https://www.bbc.com/news"
response = requests.get(website_url)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

article_tags = soup.find_all(name='h3', class_='nw-o-link-split__text')
article_texts = [text.getText() for text in article_tags]


for article in article_tags:
    text = article.getText()
    article_texts.append(text)


print(article_texts)
