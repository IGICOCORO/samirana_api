from django.db import models
from django.contrib.models import User

# Create your models here.
class Enseignement(models.Model):
    id = models.AutoField(primary_key=True)
    audio = models.FileField(uploads_to="enseignements/")
    categorie = models.ForeignKey(Category,on_delete=models.PROTECT)
    date = models.DateField(verbose_name="Date de parution", default=timezone.now)
    titre = models.CharField(max_length=40)
    
    def __str__(self):
        return f"Enseignement du {self.date}comme titre:{self.titre} categorie: {self.categorie} "
    
class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to="categorie/")
    
    def __str__(self):
        return self.name

class Annonce(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(unique=True, max_length=100)
    categorie = models.ForeignKey('Categorie', null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey('Profile', null=True, on_delete=models.SET_NULL)
    text = models.TextField()
    date = models.DateField(verbose_name="Date de parution", default=timezone.now)
    slug = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.titre
    

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    moi = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to="profile/")
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
    	return f"{self.user.first_name} {self.user.last_name}"