# Generated by Django 2.2.4 on 2020-04-23 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20200423_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='banner',
        ),
        migrations.RemoveField(
            model_name='product',
            name='banner3',
        ),
    ]