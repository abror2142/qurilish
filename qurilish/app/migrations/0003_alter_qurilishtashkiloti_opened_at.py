# Generated by Django 5.0.6 on 2024-06-03 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_qurilishtashkiloti_opened_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qurilishtashkiloti',
            name='opened_at',
            field=models.DateField(),
        ),
    ]
