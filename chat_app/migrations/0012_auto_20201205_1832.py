# Generated by Django 3.1 on 2020-12-05 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0011_auto_20201205_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heading_1',
            name='element_type',
        ),
        migrations.AddField(
            model_name='page_element',
            name='element_type',
            field=models.CharField(default='Heading_1', max_length=85),
            preserve_default=False,
        ),
    ]