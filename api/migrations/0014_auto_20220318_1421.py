# Generated by Django 3.1.5 on 2022-03-18 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20220318_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infotrafficlight',
            name='data',
            field=models.JSONField(null=True),
        ),
    ]