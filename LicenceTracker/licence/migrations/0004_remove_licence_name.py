# Generated by Django 4.1.1 on 2022-09-08 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licence', '0003_auto_20220908_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='licence',
            name='name',
        ),
    ]
