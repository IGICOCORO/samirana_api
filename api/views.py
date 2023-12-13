from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import *
from .models import *

class TokenPairView(TokenObtainPairView):
	serializer_class = TokenObtainPairSerializer

class EnseignementViewset(viewsets.ModelViewSet):
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Enseignement.objects.all()
	serializer_class = EnseignementSerializer


class CategorieViewset(viewsets.ModelViewSet):
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Categorie.objects.all()
	serializer_class = CategorieSerializer

class AnnonceViewset(viewsets.ModelViewSet):
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Annonce.objects.all()
	serializer_class = AnnonceSerializer


# class ProfileViewset(viewsets.ModelViewSet):
# 	authentication_classes = [JWTAuthentication, SessionAuthentication]
# 	permission_classes = [IsAuthenticated]
# 	queryset = Profile.objects.all()
# 	serializer_class = ProfileSerializer

