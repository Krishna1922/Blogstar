# Generated by Django 3.2.8 on 2021-12-15 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('issue', models.TextField()),
                ('phone', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
