# Generated by Django 4.0.4 on 2022-04-12 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_project', '0005_alter_usermodel_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='first_name',
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
