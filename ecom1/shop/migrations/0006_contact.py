# Generated by Django 2.2.4 on 2020-04-22 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20190306_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Subject', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('Message', models.TextField()),
            ],
        ),
    ]
