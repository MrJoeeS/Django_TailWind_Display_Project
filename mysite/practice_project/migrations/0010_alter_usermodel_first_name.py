# Generated by Django 4.0.4 on 2022-04-12 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_project', '0009_alter_usermodel_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='first_name',
            field=models.TextField(max_length=1000),
        ),
    ]
