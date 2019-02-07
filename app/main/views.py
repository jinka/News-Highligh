from flask import render_template,request,redirect,url_for
from . import main
# from  app import app
from ..request import get_sources,get_articles,search_article
from ..models import Sources


# Views
@main.route('/')
def index():
	'''
	view root page function that returns the index the page and its data
	'''
	sources = get_sources('business')
	sports_sources = get_sources('sports')
	technology_sources = get_sources('technology')
	entertainment_sources = get_sources('entertainment')
	title = "News Highlighter"

	search_movie = request.args.get('movie_query')
	if search_movie:
		return redirect(url_for('.search',movie_name=search_movie))
	else:
		return render_template('index.html',title = title, sources = sources,sports_sources = sports_sources,technology_sources = technology_sources,entertainment_sources = entertainment_sources)

@main.route('/sources/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
	title = f'NH | {id}'

	return render_template('articles.html',title= title,articles = articles)


@main.route('/search/<movie_name>')
def search(movie_name):

    '''
    View function to display the search results
    '''

    article_name_list = movie_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    title = f'search results for {movie_name}'

    return render_template('search.html',articles = searched_articles)