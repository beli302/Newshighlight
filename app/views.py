from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/news/<int:news_id>')
def news(news_id):

	'''
	Function to view news page
	'''
	news = get_news(id)
	title = f'{id}'

	return render_template('news.html',title= title,news = news_articles)


@app.route('/')
def index():

    '''
    function that returns the index page and its data
    '''

    # Getting popular movie
    general_news = get_sources('general')
    technology_news = get_sources('technology')
    business_news = get_sources('business')
    sports_news = get_sources('sports')
    entertainment_news = get_sources('entertainment')
    
    
    return render_template('index.html', title = title, general = general_news, technology = technology_news, business = business_news, sports = sports_news, entertainment = entertainment_news )
