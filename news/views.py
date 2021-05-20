from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
import json
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .scraper import scrape
from .models import *
from .forms import CreateUserForm


bbc_news = scrape("https://www.bbc.com/news", 'h3', 'nw-o-link-split__text')
nbc_news = scrape("https://www.nbcnews.com/", 'h2', 'alacarte__headline')
aljazeera = scrape("https://www.aljazeera.com/",
                   'a', 'fte-featured__title__link')
prothom_alo = scrape(
    "https://www.prothomalo.com/collection/latest", 'h2', 'headline')
manob_jomin = scrape("https://mzamin.com/category.php?cid=8", 'a', '')
kaler_kontho = scrape(
    "https://www.kalerkantho.com/online/country-news/", 'a', 'title hidden-xs')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('news:latest')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('news:login')

        context = {'form': form}
        return render(request, 'news/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('news:archive')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('news:archive')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'news/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('news:login')


def latest(request):
    context = {
        'bbc_news': bbc_news,
        'nbc_news': nbc_news,
        'aljazeera': aljazeera,
        'prothom_alo': prothom_alo,
        'manob_jomin': manob_jomin,
        'kaler_kontho': kaler_kontho
    }
    return render(request, 'news/latest.html', context)


@login_required(login_url='news:login')
def archive(request):
    news = News.objects.all()
    is_bookmarked = False
    
    for n in news:
        if n.bookmark.filter(id=request.user.id).exists():
            is_bookmarked = True

    if 'q' in request.GET:
        q = request.GET['q']
        news = News.objects.filter(headline__icontains=q) or News.objects.filter(newspaper_name__icontains=q)
    else:
        news = News.objects.all()

    context = {
        'news': news,
        'is_bookmarked': is_bookmarked
    }

    return render(request, 'news/archive.html', context)


@login_required(login_url='news:login')
def add_to_bookmark(request, id):
    card = get_object_or_404(News, id=id)
    
    if card.bookmark.filter(id=request.user.id).exists():
        card.bookmark.remove(request.user)
    else:
        card.bookmark.add(request.user)

    return HttpResponseRedirect(card.get_absolute_url())


@login_required(login_url='news:login')
def bookmark_list(request):
    user = request.user
    bookmarkList = user.bookmark.all()
    context = {
        'bookmarkList': bookmarkList
    }

    return render(request,'news/bookmarks.html', context)
