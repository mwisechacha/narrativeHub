# Generated by Django 4.2.2 on 2023-07-05 14:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stories', '0008_remove_comment_name_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_stories', to=settings.AUTH_USER_MODEL),
        ),
    ]