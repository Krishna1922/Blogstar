# Generated by Django 3.2.12 on 2023-07-12 12:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_auto_20230712_1733'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='User_profile',
        ),
    ]
