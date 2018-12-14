from django.conf.urls import url
from . import views
from django.contrib import admin
from Aboriginal.settings import MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
    url(r'^time/$', views.index, name = 'time'),
	url(r'^introduction/$', views.introduction, name = 'introduction'),
	url(r'^issue/$', views.issue, name = 'issue'),
	url(r'^$', views.index, name = 'index'),
	url(r'^hand_made/$', views.hand_made, name = 'hand_made'),
	url(r'^(?P<work_id>[0-9]+)/$', views.hand_made_detail, name='hand_made_detail'),
    url(r'^hand_made_add/$', views.hand_made_add, name = 'hand_made_add'),
	url(r'^hand_made_delete/(?P<work_id>[0-9]+)/$', views.hand_made_delete, name = 'hand_made_delete'),
	url(r'^Add_Account/$', views.Add_Account, name = 'Add_Account'),
	url(r'^Add_Issue/$', views.Add_Issue, name = 'Add_Issue'),
	# 洧彥的16個頁面
	url(r'^Amis/$', views.Amis, name = 'Amis'),
	url(r'^Bunun/$', views.Bunun, name = 'Bunun'),
	url(r'^Paiwan/$', views.Paiwan, name = 'Paiwan'),
	url(r'^Pinuyumayan/$', views.Pinuyumayan, name = 'Pinuyumayan'),
	url(r'^Rukai/$', views.Rukai, name = 'Rukai'),
	url(r'^Tayal/$', views.Tayal, name = 'Tayal'),
	url(r'^Tsou/$', views.Tsou, name = 'Tsou'),
	# url(r'Amis^/$', views.Amis, name = 'Amis'),
	# url(r'Amis^/$', views.Amis, name = 'Amis'),
	# url(r'Amis^/$', views.Amis, name = 'Amis'),
	# url(r'Amis^/$', views.Amis, name = 'Amis'),
	# url(r'Amis^/$', views.Amis, name = 'Amis'),
	# url(r'Amis^/$', views.Amis, name = 'Amis'),
	# url(r'Amis^/$', views.Amis, name = 'Amis'),
	# url(r'Amis^/$', views.Amis, name = 'Amis'),
	# url(r'Amis^/$', views.Amis, name = 'Amis'),
	#url(r'^admin/', admin.site.urls),
]