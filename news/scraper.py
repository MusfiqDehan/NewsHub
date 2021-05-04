from bs4 import BeautifulSoup
import requests


def scrape(website_url, tag_name, class_name):
    response = requests.get(website_url)
    web_page = response.text
    soup = BeautifulSoup(web_page, "html.parser")
    article_tags = soup.find_all(name=tag_name, class_=class_name)
    article_texts = [text.getText() for text in article_tags]


    for article in article_tags:
        text = article.getText()
        article_texts.append(text)

    return article_texts[1:19]


# bbc_news = scrape("https://www.bbc.com/news", 'h3', 'nw-o-link-split__text')
# nbc_news = scrape("https://www.nbcnews.com/", 'h2', 'alacarte__headline')
# aljazeera = scrape("https://www.aljazeera.com/", 'a', 'fte-featured__title__link')
# prothom_alo = scrape("https://www.prothomalo.com/collection/latest", 'h2', 'headline')
# manob_jomin = scrape("https://mzamin.com/category.php?cid=8", 'a', '')
# kaler_kontho = scrape("https://www.kalerkantho.com/online/country-news/", 'a', 'title hidden-xs')

# print(bbc_news)
# print('\n')
# print(nbc_news)
# print('\n')
# print(aljazeera)
# print('\n')
# print(prothom_alo)
# print('\n')
# print(manob_jomin)
# print('\n')
# print(kaler_kontho)
