# Generated by Django 4.0.3 on 2022-03-18 09:08

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instaclone', '0007_alter_following_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='following',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=cloudinary.models.CloudinaryField(default='images/default.jpg', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='images/default.jpg', max_length=255, null=True, verbose_name='image'),
        ),
    ]
