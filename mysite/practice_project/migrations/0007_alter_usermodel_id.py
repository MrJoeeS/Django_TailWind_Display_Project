# Generated by Django 4.0.4 on 2022-04-12 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_project', '0006_remove_usermodel_first_name_alter_usermodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='id',
            field=models.CharField(max_length=10000, primary_key=True, serialize=False),
        ),
    ]
