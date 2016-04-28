from django.conf.urls import url
from . import views
from music1 import settings
from django.conf.urls.static import static
import os

STATIC_ROOT = os.path.join(settings.BASE_DIR, 'movie_all_years/static/')

urlpatterns = [
	url(r'^2011-2015/$', views.year_2011_2015, name='index_2011_2015'),
	
	url(r'^2001-2010/$', views.year_2001_2010, name='index_2001_2010'),
		url(r'^2001-2010/year_2010/$', views.year_2010, name='year_2010'),
		
	url(r'^1991-2000/$', views.year_1991_2000, name='index_1991_2000')
] + static(settings.STATIC_URL, document_root=STATIC_ROOT)
