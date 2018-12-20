from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Works(models.Model):							#儲存手工藝品資料
	class Meta:
		permissions = (
			("add_add_works", "add_add_works"),  # 只有一個權限時，千萬不要忘了逗號！

		)
	Title = models.CharField(max_length = 25,verbose_name="手工藝標題")		#標題
	Introduction = models.TextField(blank = False,verbose_name="手工藝簡介")	#簡介
	Contact = models.TextField(blank = False,verbose_name="聯繫方式")		#聯絡資訊
	Photo = models.ImageField(upload_to = './', blank = False,verbose_name="手工藝照片")		#照片
	Add_time = models.DateTimeField(auto_now_add = True)#新增的時間
	Edit_time = models.DateTimeField(auto_now = True)#編輯的時間
	User = models.ForeignKey(User, on_delete=models.CASCADE,default="",verbose_name="手工藝新增者")

	
class Issue(models.Model):						#儲存議題資料
	# class Meta:
	# 	permissions = (
	# 		("add_issue", "add_issue"),  # 只有一個權限時，千萬不要忘了逗號！

	# 	)
	Title = models.CharField(max_length = 25,verbose_name="議題標題")	
	Context = models.TextField(blank = False,verbose_name="議題內容")
	User = models.ForeignKey(User, on_delete=models.CASCADE,default="")
	Photo = models.ImageField(upload_to = './', blank = False,verbose_name="議題照片",default='')		#照片
	Add_time = models.DateTimeField(auto_now_add = True)
	Edit_time = models.DateTimeField(auto_now = True)
	
# class Board(models.Model):						#儲存留言板資料
# 	Context = models.TextField(blank = False)
# 	User_name = models.CharField(max_length = 25)
# 	Add_time = models.DateTimeField(auto_now_add = False)
# 	Edit_time = models.DateTimeField(auto_now = False)
# 	Issue = models.ForeignKey(Issue, on_delete=models.CASCADE,default="")
