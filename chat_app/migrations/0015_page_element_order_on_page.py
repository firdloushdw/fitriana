# Generated by Django 3.1 on 2020-12-12 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0014_auto_20201206_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='page_element',
            name='order_on_page',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
