from django.conf.urls import url
from . import views
from django.contrib import admin
from Aboriginal.settings import MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
    url(r'^time/$', views.index, name = 'time'),
	url(r'^introduction/$', views.introduction, name = 'introduction'),
	url(r'^dog/$', views.dog, name = 'dog'),
	url(r'^$', views.index, name = 'index'),
	url(r'^hand_made/$', views.hand_made, name = 'hand_made'),
	url(r'^(?P<work_id>[0-9]+)/$', views.hand_made_detail, name='hand_made_detail'),

	#url(r'^admin/', admin.site.urls),
]