# Generated by Django 5.1.2 on 2024-11-03 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0004_bus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conduct',
            fields=[
                ('idConduct', models.AutoField(primary_key=True, serialize=False)),
                ('nomConduct', models.CharField(max_length=100)),
                ('prenomConduct', models.CharField(max_length=100)),
                ('emailConduct', models.CharField(max_length=100)),
            ],
        ),
    ]
