from django.contrib import admin

# Register your models here.
from .models import Works
from .models import Issue
# from .models import Board

admin.site.register(Works)
admin.site.register(Issue)
# admin.site.register(Board)
