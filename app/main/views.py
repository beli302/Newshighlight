from flask import render_template,redirect,url_for,request
from . import main
from ..request import get_articles,get_news

@main.route('/')
def index():
    '''
    Function that returns the index page and the processed data
    '''
    general_news = get_news('general')
    business_news = get_news('business')
    entertainment_news = get_news('entertainment')
    sports_news = get_news('sports')
    technology_news = get_news('technology')
   

    title = 'Home | Best News Update Site'
    
    return render_template('index.html',title=title, general=general_news, business=business_news, entertainment=entertainment_news, sports=sports_news, technology=technology_news)

@main.route('/articles/<id>')
def articles(id):
	'''
	Function to view articles page
	'''
	news_articles = get_articles(id)
	title = f'{id}'

	return render_template('news_article.html',title= title,articles = news_articles)

@main.route('/sources/<id>')
def sources(id):
	'''
	Function to view sources page
	'''
	news_sources = get_sources(id)
	title = f'{id}'

	return render_template('index.html',title= title,sources = news_es)