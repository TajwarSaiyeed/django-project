# Generated by Django 5.1.3 on 2024-11-24 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='task',
        ),
    ]
