# Generated by Django 2.2.4 on 2020-04-22 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='Phone',
        ),
    ]