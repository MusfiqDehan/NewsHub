import sqlite3
import requests
from bs4 import BeautifulSoup

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()


def checkIfExist(head):
    check = "SELECT * FROM news_news WHERE headline = ('%s')" % head
    cur.execute(check)
    return cur.rowcount


def findBySingleNews(newsLink):
    try:
        news_url = requests.get(newsLink)
        soup2 = BeautifulSoup(news_url.text, 'html.parser')
        head = soup2.find('h3', {'class': 'font-weight-bolder'})
        image = soup2.find('img', {'class': 'figure-img img-fluid rounded-0'})
        head.attrs.clear()
        head = head.getText()

        if checkIfExist(head) == 0:
            imageLink = image.get('src')
            for desc in soup2.find_all('div', {'class': 'IfTxty news-element-text text-justify my-2 pr-md-4 text-break'}):
                description = desc.getText().replace("\n", "")

                sql = "INSERT INTO news_news (headline) VALUES ('%s')" % (
                head)
                cur.execute(sql)
                conn.commit()
        else:
            return
    except:
        return


links = []

url = "https://www.bbc.com/news"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

for link in soup.find_all('a', {'class': 'text-decoration-none'}):
    l = link.get('href')
    if l == '/':
        continue
    links.append(l)
links = list(dict.fromkeys(links))
links.reverse()
while len(links) >= 10:
    findBySingleNews(links.pop())

cur.close()
conn.close()