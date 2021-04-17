from bs4 import BeautifulSoup
import requests
# import sqlite3
# import datetime

# conn = sqlite3.connect('db.sqlite3')
# c = conn.cursor()


def scrape(website_url, tag_name, class_name):
    response = requests.get(website_url)
    web_page = response.text
    soup = BeautifulSoup(web_page, "html.parser")
    article_tags = soup.find_all(name=tag_name, class_=class_name)
    article_texts = [text.getText() for text in article_tags]

    # c.execute("INSERT INTO news_news VALUES(?, ?, ?, ?, ?)", (article_texts))
    # conn.commit()
    for article in article_tags:
        text = article.getText()
        article_texts.append(text)

    return article_texts[1:19]


# bbc_news = scrape("https://www.bbc.com/news", 'h3', 'nw-o-link-split__text')
# nbc_news = scrape("https://www.nbcnews.com/", 'h2', 'alacarte__headline')
# aljazeera = scrape("https://www.aljazeera.com/", 'a', 'fte-featured__title__link')

# print(bbc_news)
# print('\n')
# print(nbc_news)
# print('\n')
# print(aljazeera)
