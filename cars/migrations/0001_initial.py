# Generated by Django 5.1.1 on 2024-10-18 19:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=250)),
                ('factory_year', models.IntegerField()),
                ('model_year', models.IntegerField()),
                ('plate', models.CharField(max_length=10)),
                ('color', models.CharField(choices=[('RED', 'Red'), ('WHITE', 'White'), ('GRAY', 'Gray'), ('SILVER', 'Silver')], max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cars', to='brands.brand')),
            ],
        ),
    ]
