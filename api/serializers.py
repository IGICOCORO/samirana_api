from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class EnseignementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Enseignement
		fields = "__all__"

class CategorieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categorie
		fields = "__all__"

class AnnonceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Annonce
		fields = "__all__"

# class ProfileSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Profile
# 		fields = "__all__"

