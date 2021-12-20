import timeit
import threading
import requests
from bs4 import BeautifulSoup
from news.models import News


# checking if that news link exists on database
def checkIfExist(newsLink):
    numOfNews = News.objects.filter(newslink=newsLink).count()
    return numOfNews


# Main news page to bring more news
def mainNewsPage(url):
    res = requests.get(url)
    return BeautifulSoup(res.text, 'html.parser')


# collect news links
def collectLinks(soup, findClass, name):
    listOfLink = []
    for findLink in soup.find_all(findClass):
        link = findLink.get('href')
        if len(str(link)) >= 45 and name.lower() in link:
            listOfLink.append(link)
    links = list(dict.fromkeys(listOfLink))  # remove same link
    links.reverse()
    return links


# save to database
def saveToDB(head, imageLink, newsLink, desc, name):
    if desc != '' and len(head) < 90:
        news = News(heading=head, imagelink=imageLink,
                    newslink=newsLink, details=desc, papername=name)
        news.save()
        print(head)


# web scraping Jugantor
def jugantor():
    name = 'Jugantor'
    url = 'https://www.jugantor.com/all-news'

    findClass = 'a', {'class': 'text-decoration-none'}
    soup = mainNewsPage(url)
    links = collectLinks(soup, findClass, name)

    while len(links) > 0:
        newsLink = links.pop()
        try:
            if checkIfExist(newsLink) == 0:
                news_url = requests.get(newsLink)
                soup = BeautifulSoup(news_url.text, 'html.parser')

                headdiv = soup.find('h3', {'class': 'font-weight-bolder'})
                head = headdiv.getText()

                imagediv = soup.find(
                    'img', {'class': 'figure-img img-fluid rounded-0'})
                imageLink = imagediv.get('src')

                desc = ''
                for i in soup.find_all('div',
                                       {'class': 'IfTxty news-element-text text-justify my-2 pr-md-4 text-break'}):
                    desc = i.getText().replace("\n", "")

                saveToDB(head, imageLink, newsLink, desc, name)
            else:
                break
        except Exception:
            continue


# web scraping Samakal
def samakal():
    name = 'Samakal'
    url = 'https://samakal.com/list/all'

    findClass = 'a', {'class': 'link-overlay'}
    links = collectLinks(mainNewsPage(url), findClass, name)

    while len(links) > 0:
        newsLink = links.pop()
        try:
            if checkIfExist(newsLink) == 0:
                news_url = requests.get(newsLink)
                soup = BeautifulSoup(news_url.text, 'html.parser')

                headdiv = soup.find('h1', {'class': 'detail-headline'})
                head = headdiv.getText()

                imagediv = soup.find('div', {'class': 'lightgallery'})
                image = imagediv.find('img', {'class': 'img-responsive'})
                imageLink = image.get('src')

                desc = ''
                body = soup.find('div', {'class': 'description'})
                for i in body.find_all('span'):
                    desc += i.getText().replace("\n", "")

                saveToDB(head, imageLink, newsLink, desc, name)
            else:
                break
        except Exception:
            continue


# web scraping Ittefaq
def ittefaq():
    name = 'Ittefaq'
    url = 'https://www.ittefaq.com.bd/all-news'

    findClass = 'a', {'class': None}
    links = collectLinks(mainNewsPage(url), findClass, name)

    while len(links) > 0:
        newsLink = links.pop()
        try:
            if checkIfExist(newsLink) == 0:
                news_url = requests.get(newsLink)
                soup = BeautifulSoup(news_url.text, 'html.parser')

                headdiv = soup.find('div', {'id': 'dtl_hl_block'})
                head = headdiv.getText()

                imagediv = soup.find('div', {'id': 'dtl_img_block'})
                image = imagediv.find('img')
                imageLink = "https://www.ittefaq.com.bd" + image.get('src')

                desc = ''
                body = soup.find('div', {'id': 'dtl_content_block'})
                for i in body.find_all('p'):
                    desc += i.getText().replace("\n", "")

                saveToDB(head, imageLink, newsLink, desc, name)
            else:
                break
        except Exception:
            continue


# Start scraping
def Scrape():
    start = timeit.default_timer()

    print("______________Initialized Scrape_________________")
    p1 = threading.Thread(target=jugantor())
    p2 = threading.Thread(target=samakal())
    p3 = threading.Thread(target=ittefaq())

    p1.start()
    p2.start()
    p3.start()

    stop = timeit.default_timer()
    print('Time: ', stop - start)
