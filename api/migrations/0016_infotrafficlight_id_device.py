# Generated by Django 3.1.5 on 2022-04-14 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20220318_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='infotrafficlight',
            name='id_device',
            field=models.CharField(default='0', max_length=100, verbose_name='Айди устройства'),
        ),
    ]