from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
import datetime
# Create your views here.
from .models import Works

# View(views.py)

# 用template
def introduction(request):
	return render(request, 'omniscient/introduction.html')
	
def dog(request):
	return render(request, 'omniscient/dog.html')
	
def index(request):
	return render(request, 'omniscient/index.html')
	
def hand_made(request):
	works = Works.objects.all()
	return render(request, 'omniscient/hand_made.html', {'works': works})

def hand_made_detail(request, work_id):
    work = get_object_or_404(Works, pk=work_id)
    return render(request, 'omniscient/hand_made_detail.html', {'work': work})