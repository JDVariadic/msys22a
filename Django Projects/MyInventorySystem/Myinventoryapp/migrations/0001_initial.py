# Generated by Django 3.0.2 on 2020-03-03 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WaterBottle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=300)),
                ('brand', models.CharField(max_length=300)),
                ('cost', models.FloatField()),
                ('size', models.CharField(max_length=300)),
                ('mouthSize', models.CharField(max_length=300)),
                ('color', models.CharField(max_length=300)),
                ('currentQuantity', models.FloatField()),
                ('suppliedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myinventoryapp.Supplier')),
            ],
        ),
    ]
