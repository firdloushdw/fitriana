# Generated by Django 3.1 on 2021-03-06 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0061_page_element_column'),
    ]

    operations = [
        migrations.AddField(
            model_name='kanban_group',
            name='color',
            field=models.CharField(default='red', max_length=100),
            preserve_default=False,
        ),
    ]
