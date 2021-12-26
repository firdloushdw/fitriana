# Generated by Django 3.1 on 2020-12-05 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0006_auto_20201125_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page_element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat_app.page')),
            ],
        ),
        migrations.CreateModel(
            name='Heading_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_text', models.CharField(max_length=85)),
                ('page_element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat_app.page_element')),
            ],
        ),
    ]
