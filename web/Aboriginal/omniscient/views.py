from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
from .models import Works

# View(views.py)
def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

# 用template
def cat(request):
	return render(request, 'omniscient/cat.html')
	
def dog(request):
	return render(request, 'omniscient/dog.html')
	
def about(request):
	return render(request, 'omniscient/about.html')
	
def hand_made(request):
	works = Works.objects.all()
	return render(request, 'omniscient/hand_made.html', {'works': works})