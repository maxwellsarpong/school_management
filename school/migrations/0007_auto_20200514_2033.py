# Generated by Django 3.0.5 on 2020-05-14 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_auto_20200424_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fees',
            old_name='f_stu',
            new_name='f_stu_id',
        ),
    ]
