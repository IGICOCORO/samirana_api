# Generated by Django 4.2.7 on 2023-12-13 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='categorie/')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('moi', models.TextField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(upload_to='profile/')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Enseignement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('audio', models.FileField(upload_to='enseignements/')),
                ('date', models.DateField(verbose_name='Date de parution')),
                ('titre', models.CharField(max_length=40)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=100, unique=True)),
                ('text', models.TextField()),
                ('date', models.DateField(verbose_name='Date de parution')),
                ('slug', models.CharField(blank=True, max_length=1000, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.profile')),
                ('categorie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.categorie')),
            ],
        ),
    ]
