# Generated by Django 3.0.5 on 2020-04-21 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parent',
            old_name='guardian',
            new_name='stu',
        ),
    ]
