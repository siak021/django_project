# Generated by Django 5.1 on 2024-08-29 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='text',
            field=models.TextField(),
        ),
    ]
