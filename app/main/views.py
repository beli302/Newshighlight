from flask import render_template,redirect,url_for,request
from . import main
from ..models import Sources,Articles
from ..request import get_articles,get_sources

@main.route('/')
def index():
    '''
    Function that returns the index page and the processed data
    '''
    general_news = get_sources('general')
    business_news = get_sources('business')
    entertainment_news = get_sources('entertainment')
    sports_news = get_sources('sports')
    technology_news = get_sources('technology')
   

    title = 'Home | Best News Update Site'
    
    return render_template('index.html',title=title, general=general_news, business=business_news, entertainment=entertainment_news, sports=sports_news, technology=technology_news)

@main.route('/articles/<id>')
def articles(id):
	'''
	Function to view articles page
	'''
	news_articles = get_articles(id)
	title = f'{id}'

	return render_template('articles.html',title= title,articles = news_articles)