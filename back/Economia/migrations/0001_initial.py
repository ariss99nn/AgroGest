# Generated by Django 5.2.1 on 2025-06-24 02:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Siembra', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='EconomicIndicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.FloatField()),
                ('source', models.CharField(max_length=200)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EconomicCalculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimated_investment', models.DecimalField(decimal_places=2, max_digits=12)),
                ('projected_income', models.DecimalField(decimal_places=2, max_digits=12)),
                ('irr', models.FloatField(blank=True, null=True)),
                ('npv', models.FloatField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sowing', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Siembra.sowing')),
            ],
        ),
    ]
