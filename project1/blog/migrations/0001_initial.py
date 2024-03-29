# Generated by Django 3.2.12 on 2023-07-11 16:08

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(blank=True, max_length=50)),
                ('Title', models.CharField(max_length=50)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Time', models.DateTimeField(default=datetime.datetime.now)),
                ('Tag', models.CharField(choices=[('Film & Animation', 'Film & Animation'), ('Autos & Vehicles', 'Autos & Vehicles'), ('Music', 'Music'), ('Pets & Animals', 'Pets & Animals'), ('Sports', 'Sports'), ('Travel & Events', 'Travel & Events'), ('Gaming', 'Gaming'), ('People & Blogs', 'People & Blogs'), ('Comedy', 'Comedy'), ('Entertainment', 'Entertainment'), ('News & Politics', 'News & Politics'), ('Howto & Style', 'Howto & Style'), ('Education', 'Education'), ('Science & Technology', 'Science & Technology'), ('Nonprofits & Activism', 'Nonprofits & Activism')], default='Web_Development', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('Timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('Commentpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='blog.comment')),
            ],
            options={
                'ordering': ['-Timestamp'],
            },
        ),
    ]
