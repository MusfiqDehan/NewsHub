from bs4 import BeautifulSoup
import requests
import sqlite3

# conn = sqlite3.connect('newshub.sqlite3')
# c = conn.cursor()

# c.execute("CREATE TABLE news1(title TEXT, link TEXT, images TEXT)")


website_url = "https://www.bbc.com/news"
response = requests.get(website_url)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")


article_texts = []
article_links = []
article_images = []
site_names = ['BBC News', 'NBC News', 'Aljazeera']


article_tags = soup.find_all(name='a', class_='gs-c-promo-heading')

for article in article_tags:
    text = article.getText()
    article_texts.append(text)

    link = article.get("href")
    article_links.append(link)



images = soup.find_all(name='img')

for image in images:
    article_images.append(image['src'])



for i in range(10):
    print(article_texts[i])
    print("https://www.bbc.com"+article_links[i])
    print(article_images[i])
    print('\n')
    # c.execute("INSERT INTO news1 VALUES(?, ?, ?)", (article_texts[i], "https://www.bbc.com"+article_links[i], article_images[i]))
    # conn.commit()


# conn.close()
# c.close()