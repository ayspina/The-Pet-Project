# Generated by Django 4.1.5 on 2023-01-20 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_resource_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='type',
            field=models.CharField(max_length=10),
        ),
    ]
