# Generated by Django 3.2 on 2021-08-09 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.FileField(blank=True, default='blog-1.jpg', null=True, upload_to='blog/image'),
        ),
    ]
