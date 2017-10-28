from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Organisation)
admin.site.register(Category_contest)
admin.site.register(Contest)