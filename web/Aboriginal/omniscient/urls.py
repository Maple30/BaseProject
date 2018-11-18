from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^time/$', views.index, name = 'time'),
	url(r'^cat/$', views.cat, name = 'cat'),
	url(r'^dog/$', views.dog, name = 'dog'),
	url(r'^about/$', views.about, name = 'about'),
	url(r'^hand_made/$', views.hand_made, name = 'hand_made'),
    #url(r'^admin/', admin.site.urls),
]
