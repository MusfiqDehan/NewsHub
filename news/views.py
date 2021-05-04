from django.http import HttpResponse
from django.shortcuts import render
import itertools
from .scraper import scrape


bbc_news = scrape("https://www.bbc.com/news", 'h3', 'nw-o-link-split__text')
nbc_news = scrape("https://www.nbcnews.com/", 'h2', 'alacarte__headline')
aljazeera = scrape("https://www.aljazeera.com/", 'a', 'fte-featured__title__link')
prothom_alo = scrape("https://www.prothomalo.com/collection/latest", 'h2', 'headline')
manob_jomin = scrape("https://mzamin.com/category.php?cid=8", 'a', '')
kaler_kontho = scrape("https://www.kalerkantho.com/online/country-news/", 'a', 'title hidden-xs')

app_name = 'news'

zipped_data = zip(bbc_news, nbc_news, aljazeera, prothom_alo, manob_jomin, kaler_kontho)

def index(request):
    return render(request, 'news/home.html', 
    {
        'bbc_news': bbc_news, 
        'nbc_news': nbc_news, 
        'aljazeera': aljazeera,
        'prothom_alo': prothom_alo,
        'manob_jomin': manob_jomin,
        'kaler_kontho': kaler_kontho
    })
