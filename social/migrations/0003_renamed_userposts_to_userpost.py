# Generated by Django 2.1.4 on 2019-01-07 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_userposts'),
    ]

    operations = [
        migrations.RenameModel('UserPosts', 'UserPost'),
    ]
