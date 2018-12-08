from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import permission_required, login_required
# Create your views here.
from .models import Works
from .forms import WorksForm

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


@login_required
@permission_required('omniscient.add_works')
def hand_made_add(request):
	if request.method == "POST":
		form = WorksForm(request.POST,request.FILES)
		if form.is_valid():
			work = form.save(commit=False)
			work.User = request.user
			work.save()
			return redirect('hand_made')
	else:
		form = WorksForm()
	return render(request, 'omniscient/forms.html', {'form': form})
