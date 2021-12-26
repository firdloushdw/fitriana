# Generated by Django 3.1 on 2021-02-06 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0034_to_do'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table', to='chat_app.page_element')),
            ],
        ),
    ]