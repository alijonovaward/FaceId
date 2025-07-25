# Generated by Django 5.1.11 on 2025-06-11 06:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dormitory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dormitories', to='accounts.director')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddress', models.GenericIPAddressField()),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('entrance', models.BooleanField(default=True)),
                ('dormitory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='dormitory.dormitory')),
            ],
        ),
    ]
