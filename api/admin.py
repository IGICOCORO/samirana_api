from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Enseignement)
class EnseignementAdmin(admin.ModelAdmin):
	list_display = "id", "name", "audio", "categorie", "date", "titre"
	list_filter = "id", "categorie", "date"
	search_fields = "id", "name", "audio", "categorie", "date", "titre"
 
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
	list_display = "id", "titre","categorie","author","text","date","slug"
	list_filter =  "id","categorie","author","date"
	search_fields =  "id", "titre","categorie","author","date",
@admin.register(Annonce)
class AnnonceAdmin(admin.ModelAdmin):
	list_display = "id", "name","image"
	list_filter = "id", "name", 
	search_fields = "id", "name"
@admin.register(Profile)
class AnnonceAdmin(admin.ModelAdmin):
	list_display = "id", "user","moi","image","birth_date"
	list_filter = "id", "user","moi","image","birth_date"
	search_fields = "id", "birth_date","user"