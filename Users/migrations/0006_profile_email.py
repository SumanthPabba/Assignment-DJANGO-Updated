# Generated by Django 4.1.3 on 2022-12-06 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_alter_profile_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='xyz@gmail.com', max_length=254),
        ),
    ]
