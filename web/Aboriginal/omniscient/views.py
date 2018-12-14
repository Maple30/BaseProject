from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import permission_required, login_required
# Create your views here.
from .models import Works
from .forms import WorksForm, UserForm, IssueForm
# from django.contrib.messages import constants as messages
from django.contrib import messages

# View(views.py)

# 用template


def introduction(request):
	return render(request, 'omniscient/introduction.html')


def issue(request):
	return render(request, 'omniscient/issue.html')

def index(request):
	return render(request, 'omniscient/index.html')


def hand_made(request):
	works = Works.objects.all()
	return render(request, 'omniscient/hand_made.html', {'works': works})


def hand_made_detail(request, work_id):
    work = get_object_or_404(Works, pk=work_id)
    return render(request, 'omniscient/hand_made_detail.html', {'work': work})

def Add_Account(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.set_password(user.password)
			user.save()
			messages.success(request, '帳戶已新增')
			return redirect('index')
	else:
		form = UserForm()
	return render(request, 'omniscient/forms.html', {'form': form})


@login_required
@permission_required('omniscient.add_works')
def hand_made_add(request):
	if request.method == "POST":
		form = WorksForm(request.POST,request.FILES)
		if form.is_valid():
			work = form.save(commit=False)
			work.User = request.user
			work.save()
			messages.success(request, '手工藝品已新增')
			return redirect('hand_made')
	else:
		form = WorksForm()
	return render(request, 'omniscient/forms.html', {'form': form})

@login_required
@permission_required('omniscient.delete_works')
def hand_made_delete(request, work_id):
    works = get_object_or_404(Works, pk=work_id)
    if(request.user != works.User):
    	return redirect('index')
    works.delete()
    messages.success(request, '手工藝品已刪除')
    return redirect('hand_made')

@login_required
@permission_required('omniscient.add_issue')
def Add_Issue(request):
	if request.method == "POST":
		form = IssueForm(request.POST)
		if form.is_valid():
			issue = form.save(commit=False)
			issue.User = request.user
			issue.save()
			messages.success(request, '議題已新增')
			return redirect('issue')
	else:
		form = IssueForm()
	return render(request, 'omniscient/forms.html', {'form': form})


# 洧彥的頁面
#1
def Amis(request):
	return render(request, 'omniscient/Amis.html')
#2	
def Bunun(request):
	return render(request, 'omniscient/Bunun.html')
#3
def Paiwan(request):
	return render(request, 'omniscient/Paiwan.html')
#4
def Pinuyumayan(request):
	return render(request, 'omniscient/Pinuyumayan.html')
#5
def Rukai(request):
	return render(request, 'omniscient/Rukai.html')
#6	
def Tayal(request):
	return render(request, 'omniscient/Tayal.html')
#7
def Tsou(request):
	return render(request, 'omniscient/Tsou.html')
#8
# def index(request):
# 	return render(request, 'omniscient/index.html')
# #9
# def index(request):
# 	return render(request, 'omniscient/index.html')
# #10	
# def index(request):
# 	return render(request, 'omniscient/index.html')
# #11
# def index(request):
# 	return render(request, 'omniscient/index.html')
# #12
# def index(request):
# 	return render(request, 'omniscient/index.html')
# #13
# def index(request):
# 	return render(request, 'omniscient/index.html')
# #14
# def index(request):
# 	return render(request, 'omniscient/index.html')
# #15
# def index(request):
# 	return render(request, 'omniscient/index.html')
# #16
# def index(request):
# 	return render(request, 'omniscient/index.html')