# Generated by Django 3.1 on 2021-02-17 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0055_tag_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='table_data',
            name='width',
            field=models.IntegerField(default=200),
            preserve_default=False,
        ),
    ]
