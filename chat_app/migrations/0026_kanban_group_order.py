# Generated by Django 3.1 on 2021-01-30 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0025_kanban_card_order_on_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='kanban_group',
            name='order',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
