from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import permission_required, login_required
# Create your views here.
from .models import Works,Issue
from .forms import WorksForm, UserForm, IssueForm
# from django.contrib.messages import constants as messages
from django.contrib import messages
from django.contrib.auth.models import Permission

# View(views.py)

# 用template


def introduction(request):
	return render(request, 'omniscient/introduction.html')


def issue(request):
	issues = Issue.objects.all()
	return render(request, 'omniscient/issue.html', {'issues': issues})

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
			per_add_issue = Permission.objects.get(codename='add_issue')
			per_del_issue = Permission.objects.get(codename='delete_issue')
			per_add_works = Permission.objects.get(codename='add_works')
			per_del_works = Permission.objects.get(codename='delete_works')
			user.user_permissions.add(per_add_issue,per_del_issue,per_add_works,per_del_works)
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
		form = IssueForm(request.POST,request.FILES)
		if form.is_valid():
			issue = form.save(commit=False)
			issue.User = request.user
			issue.save()
			messages.success(request, '議題已新增')
			return redirect('issue')
	else:
		form = IssueForm()
	return render(request, 'omniscient/forms.html', {'form': form})

@login_required
@permission_required('omniscient.delete_issue')
def issue_delete(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    if(request.user != issue.User):
    	return redirect('index')
    issue.delete()
    messages.success(request, '議題已刪除')
    return redirect('issue')


# 洧彥的頁面
#1
def Amis(request):
	return render(request, 'omniscient/Amis.html')
#2	
def Tayal(request):
	return render(request, 'omniscient/Tayal.html')

#3
def Paiwan(request):
	return render(request, 'omniscient/Paiwan.html')
#4
def Bunun(request):
	return render(request, 'omniscient/Bunun.html')
#5
def Pinuyumayan(request):
	return render(request, 'omniscient/Pinuyumayan.html')
#6	
def Rukai(request):
	return render(request, 'omniscient/Rukai.html')
#7
def Tsou(request):
	return render(request, 'omniscient/Tsou.html')
#8
def SaySiyat(request):
 	return render(request, 'omniscient/SaySiyat.html')
#9
def Yami(request):
 	return render(request, 'omniscient/Yami.html')
#10	
def Thao(request):
 	return render(request, 'omniscient/Thao.html')
#11
def Kavalan(request):
	return render(request, 'omniscient/Kavalan.html')
#12
def Taroko(request):
	return render(request, 'omniscient/Taroko.html')
#13
def Sakizaya(request):
	return render(request, 'omniscient/Sakizaya.html')
#14
def Seediq(request):
	return render(request, 'omniscient/Seediq.html')
#15
def Saaroa(request):
	return render(request, 'omniscient/Saaroa.html')
#16
def Kanakanavu(request):
	return render(request, 'omniscient/Kanakanavu.html')