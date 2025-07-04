# Generated by Django 5.2.1 on 2025-06-24 02:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variety', models.CharField(max_length=100)),
                ('classification', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('estimated_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Harvest_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimated_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('profit_margin', models.FloatField()),
                ('overall_quality', models.CharField(max_length=100)),
                ('diagram_data', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cosecha.classification')),
            ],
        ),
        migrations.CreateModel(
            name='Harvest_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('season', models.CharField(default='2025-A', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cosecha.classification')),
            ],
        ),
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.FloatField()),
                ('harvest_method', models.CharField(choices=[('MANUAL', 'Manual'), ('MECANIZED', 'Mechanized')], max_length=20)),
                ('season', models.CharField(default='2025-A', max_length=20)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cosecha.harvest_type')),
            ],
        ),
    ]
