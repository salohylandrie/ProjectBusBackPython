# Generated by Django 5.1.2 on 2024-11-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0006_relatbustrajet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='admin_code',
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
