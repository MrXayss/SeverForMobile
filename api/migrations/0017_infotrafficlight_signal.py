# Generated by Django 3.1.5 on 2022-04-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_infotrafficlight_id_device'),
    ]

    operations = [
        migrations.AddField(
            model_name='infotrafficlight',
            name='signal',
            field=models.CharField(max_length=100, null=True, verbose_name='Сигнал светофора'),
        ),
    ]