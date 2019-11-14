from django.contrib import admin
from .models import users,expense,category
# Register your models here.
admin.site.register(users)
admin.site.register(expense)
admin.site.register(category)