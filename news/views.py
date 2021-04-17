from django.http import HttpResponse
from django.shortcuts import render
from .scraper import scrape

bbc_news = scrape("https://www.bbc.com/news", 'h3', 'nw-o-link-split__text')
nbc_news = scrape("https://www.nbcnews.com/", 'h2', 'alacarte__headline')
aljazeera = scrape("https://www.aljazeera.com/", 'a', 'fte-featured__title__link')

app_name = 'news'

def index(request):
    return render(request, 'news/index.html', {'nbc_news': nbc_news})