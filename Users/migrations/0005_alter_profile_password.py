# Generated by Django 4.1.3 on 2022-11-27 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]