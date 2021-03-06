# Generated by Django 3.1 on 2021-02-12 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0048_auto_20210212_0054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('table_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='chat_app.table_data')),
            ],
        ),
    ]
