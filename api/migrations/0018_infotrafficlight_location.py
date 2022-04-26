# Generated by Django 3.1.5 on 2022-04-14 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_infotrafficlight_signal'),
    ]

    operations = [
        migrations.AddField(
            model_name='infotrafficlight',
            name='location',
            field=models.CharField(max_length=100, null=True, verbose_name='Местоположение светофора'),
        ),
    ]