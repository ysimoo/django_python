from django.contrib import admin
from models import Cours

class AuthorAdmin(admin.ModelAdmin):
	pass
admin.site.register(Cours,AuthorAdmin)

