from flask import render_template,request,redirect,url_for
from . import main
from newsapi import NewsApiClient
from ..request import get_sources, get_article,get_source_article
from ..models import News_source,News_article

@main.route('/')
def index():
    general_news = get_sources('general')

    title = 'News Highlights'
    return render_template('index.html', title = title, general=general_news)

@main.route('/top-headlines')
def news_articles():
    cnn = get_article('cnn')
    al_jazeera = get_article('al-jazeera-english')
    cbs_news = get_article('cbs-news')
    fox_news = get_article('fox-news')
    usa_today = get_article('usa-today')

    return render_template('articles.html',cnn=cnn, al_jazeera=al_jazeera,cbs_news=cbs_news,fox_news=fox_news,usa_today=usa_today)

@main.route('/articles/<id>')
def source_art(id):
    title = f'{id} | News Articles'
    sources = get_source_article(id)

    return render_template('sourcearticle.html', title= title, sources=sources)