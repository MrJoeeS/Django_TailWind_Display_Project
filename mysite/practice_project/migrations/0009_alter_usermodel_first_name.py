# Generated by Django 4.0.4 on 2022-04-12 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_project', '0008_usermodel_first_name_alter_usermodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='first_name',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
