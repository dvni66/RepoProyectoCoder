# Generated by Django 3.2.9 on 2021-12-15 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_auto_20211214_2031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movieinfo',
            old_name='category',
            new_name='categiria',
        ),
        migrations.RenameField(
            model_name='movieinfo',
            old_name='image',
            new_name='imagen',
        ),
        migrations.RemoveField(
            model_name='movieinfo',
            name='viewsCount',
        ),
    ]
