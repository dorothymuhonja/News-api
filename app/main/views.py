from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources, get_article,get_source_article
from ..models import News_source,News_article

@main.route('/')
def index():
    general_news = get_sources('general')
    sports_news = get_sources('sports')
    technology_news = get_sources('technology')
    entertainment_news = get_sources('entertainment')
    business_news = get_sources('business')
    science_news = get_sources('science')
    
    return render_template('index.html', general=general_news,sports=sports_news,technology=technology_news,entertainment=entertainment_news,business=business_news,science=science_news)

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
    sources = get_source_article(id)
    return render_template('sourcearticle.html',sources=sources)