from django.shortcuts import render_to_response
from .models import Movie, Song 
import os

def gen_list(mov_year):
	movies = Movie.objects.all().filter(year=mov_year)
	list_m = []
	songs_count = []
	count = 0
	
	for film in movies:
		list = []
		songs = Song.objects.filter(movie_id=film.id)
		list_m.append(film)
		for i in songs:
			count += 1
			list.append(count)
		zipped = zip(songs, list)
		songs_count.append(zipped)

	return list_m, songs_count

def year_2011_2015(request):
	return render_to_response('movie_all_years/year2011-2015/index.html',{'request':request})

def year_2001_2010(request):
	return render_to_response('movie_all_years/year2001-2010/index.html',{'request':request})

def year_1991_2000(request):
	return render_to_response('movie_all_years/year1991-2000/index.html',{'request':request})

def year_2010(request): 
	list, info = gen_list(2010)
	return render_to_response('movie_all_years/year2001-2010/year_2010.html',{
		"list": list,
		"info": info,
		'request':request
	})
