# Generated by Django 4.2.2 on 2023-07-03 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0006_alter_comment_options_remove_comment_author_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='comment_section',
        ),
    ]
