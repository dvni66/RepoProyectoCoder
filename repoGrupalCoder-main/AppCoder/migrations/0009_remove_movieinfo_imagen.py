# Generated by Django 3.2.9 on 2021-12-15 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0008_movieinfo_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movieinfo',
            name='imagen',
        ),
    ]
