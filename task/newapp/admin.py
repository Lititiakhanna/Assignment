from django.contrib import admin
from .models import Blog, Account, Comment

admin.site.register(Account)
admin.site.register(Blog)
admin.site.register(Comment)

# Register your models here.
