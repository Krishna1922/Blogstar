# Generated by Django 3.2.8 on 2021-12-15 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('Time', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='issue',
            new_name='Issue',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='Phone',
        ),
    ]
