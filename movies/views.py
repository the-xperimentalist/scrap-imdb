from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.template import loader
from .models import movie
import requests
from bs4 import BeautifulSoup
from .scrap import get_movie_titles, get_movie_description, get_directors, get_year, get_img_href

def index(request):
	page = requests.get('https://www.imdb.com/list/ls027892806')

	all_movie_titles = get_movie_titles(page)
	all_movie_description = get_movie_description(page)
	all_movie_directors = get_directors(page)
	all_movie_year = get_year(page)
	all_movie_img_href = get_img_href(page)

	all_movie_details = []

	length = len(all_movie_titles)
	for i in range(length):
		movie = {}
		title = all_movie_titles[i]
		description = all_movie_description[i]
		director = all_movie_directors[i]
		year = all_movie_year[i]
		img_href = all_movie_img_href[i]
		all_movie_details.append({
			"movie_title": title,
			"movie_description": description,
			"movie_director": director,
			"movie_year": year,
			"movie_img_href": img_href
			})

	return render(request, 'movies/index.html', {'all_movie_details': all_movie_details})

