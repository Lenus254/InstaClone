# Generated by Django 3.2.4 on 2022-03-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaclone', '0005_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='following',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
