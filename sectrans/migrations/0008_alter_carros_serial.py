# Generated by Django 5.1.2 on 2024-10-24 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectrans', '0007_carros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carros',
            name='serial',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]