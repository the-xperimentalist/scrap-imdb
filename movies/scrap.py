from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.imdb.com/list/ls027892806')

def get_movie_titles(page):

	bs = BeautifulSoup(page.content, "lxml")
	ta_divs = bs.find_all("div", class_="lister-item-content")

	movie_title_list = []

	for ta in ta_divs:
		ta_h2 = ta.find("h3",class_="lister-item-header")
		ta_title = ta_h2.find("a")
		movie_title_list.append(ta_title.text)

	return movie_title_list

def get_movie_description(page):
	bs = BeautifulSoup(page.content, "lxml")
	ta_divs = bs.find_all("div", class_="lister-item-content")

	movie_descripts = []

	for ta in ta_divs:
		ta_p = ta.find_all("p")
		ta_p_desc = ta_p[1]
		movie_descripts.append(ta_p_desc.text)

	return movie_descripts

def get_directors(page):
	bs = BeautifulSoup(page.content, "lxml")
	ta_divs = bs.find_all("div", class_="lister-item-content")

	movie_director = []

	for ta in ta_divs:
		ta_p = ta.find_all("p")
		ta_p_desc = ta_p[2]
		ta_p_a = ta_p_desc.find("a")
		movie_director.append(ta_p_a.text)

	return movie_director

def get_year(page):
	bs = BeautifulSoup(page.content, "lxml")
	ta_divs = bs.find_all("div", class_="lister-item-content")

	movie_year = []
	for ta in ta_divs:
		ta_h2 = ta.find("h3",class_="lister-item-header")
		ta_span = ta_h2.find("span",class_="lister-item-year")
		movie_year.append(ta_span.text)

	return movie_year

def get_img_href(page):
	bs = BeautifulSoup(page.content, "lxml")
	ta_divs = bs.find_all("div", class_="lister-item-image")

	movie_img_href = []
	for ta in ta_divs:
		ta_a = ta.find("a")
		ta_img = ta_a.find("img")
		ta_img_src = ta_img.get('src')
		movie_img_href.append(ta_img_src)

	return movie_img_href











