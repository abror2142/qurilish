# Generated by Django 5.0.6 on 2024-06-03 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qurilishtashkiloti',
            name='opened_at',
            field=models.DateTimeField(),
        ),
    ]