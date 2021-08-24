# Generated by Django 3.2 on 2021-07-15 19:44

import autoslug.fields
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
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=250)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='titre', unique=True)),
                ('description', models.TextField()),
                ('image', models.FileField(default='blog-1.jpg', upload_to='blog/image')),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('auteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auteur_article', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]