# Generated by Django 4.1.3 on 2022-11-28 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0009_alter_otherdetails_address_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='otherDetails',
        ),
    ]
