from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Works(models.Model):							#儲存手工藝品資料
	Title = models.CharField(max_length = 25)		#標題
	Introduction = models.TextField(blank = False)	#簡介
	Contact = models.TextField(blank = False)		#聯絡資訊
	Photo = models.ImageField(upload_to = './', blank = False)		#照片
	Add_time = models.DateTimeField(auto_now_add = True)#新增的時間
	Edit_time = models.DateTimeField(auto_now = True)#編輯的時間
	User = models.ForeignKey(User, on_delete=models.CASCADE,default="")

	
class Issue(models.Model):						#儲存議題資料
	Title = models.CharField(max_length = 25)	
	Context = models.TextField(blank = False)
	User = models.ForeignKey(User, on_delete=models.CASCADE,default="")
	Add_time = models.DateTimeField(auto_now_add = False)
	Edit_time = models.DateTimeField(auto_now = False)
	
# class Board(models.Model):						#儲存留言板資料
# 	Context = models.TextField(blank = False)
# 	User_name = models.CharField(max_length = 25)
# 	Add_time = models.DateTimeField(auto_now_add = False)
# 	Edit_time = models.DateTimeField(auto_now = False)
# 	Issue = models.ForeignKey(Issue, on_delete=models.CASCADE,default="")
