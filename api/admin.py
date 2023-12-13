from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Enseignement)
class EnseignementAdmin(admin.ModelAdmin):
	list_display = "id","audio", "categorie", "date", "titre"
	list_filter = "id", "categorie", "date"
	search_fields = "id", "name", "audio", "categorie", "date", "titre"
 
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
	list_display = "id", "name"
	list_filter =  "id", "name"
	search_fields =  "name",
@admin.register(Annonce)
class AnnonceAdmin(admin.ModelAdmin):
	list_display =  "titre",
	list_filter = "id",
	search_fields = "id", "titre"
 
# @admin.register(Profile)
# class AnnonceAdmin(admin.ModelAdmin):
# 	list_display = "id", "user","moi","image","birth_date"
# 	list_filter = "id", "user","moi","image","birth_date"
# 	search_fields = "id", "birth_date","user"