# Generated by Django 3.1 on 2021-02-11 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0045_auto_20210211_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table_data',
            old_name='description',
            new_name='text',
        ),
    ]