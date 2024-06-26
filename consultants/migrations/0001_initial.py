# Generated by Django 5.0 on 2024-06-10 20:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('level', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='expert', to='customer.customuser')),
                ('skills', models.ManyToManyField(related_name='experts', to='consultants.skill')),
            ],
        ),
    ]
