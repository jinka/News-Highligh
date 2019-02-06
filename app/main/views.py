from flask import render_template,request,redirect,url_for
from app import app
from ..request import get_sources,get_articles
from ..models import Sources

# Views
@app.route('/')
def index():
	'''
	view root page function that returns the index the page and its data
	'''
	sources = get_sources('business')
	sports_sources = get_sources('sports')
	technology_sources = get_sources('technology')
	entertainment_sources = get_sources('entertainment')
	title = "News Highlighter"

	return render_template('index.html',title = title, sources = sources,sports_sources = sports_sources,technology_sources = technology_sources,entertainment_sources = entertainment_sources)

@app.route('/sources/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
	title = f'NH | {id}'

	return render_template('articles.html',title= title,articles = articles)


@app.route('/search/<article_name>')
def search(article_name):

    '''
    View function to display the search results
    '''

    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    title = f'search results for {article_name}'

    return render_template('search.html',articles = searched_articles)