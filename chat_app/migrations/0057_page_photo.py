# Generated by Django 3.1 on 2021-02-18 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0056_table_data_width'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='photo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
