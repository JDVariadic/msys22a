# Generated by Django 3.0.2 on 2020-03-03 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myinventoryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waterbottle',
            name='currentQuantity',
            field=models.IntegerField(),
        ),
    ]
