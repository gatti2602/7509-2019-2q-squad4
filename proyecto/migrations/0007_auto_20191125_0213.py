# Generated by Django 2.2.5 on 2019-11-25 02:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('proyecto', '0006_auto_20191125_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riesgo',
            name='presentado',
            field=models.BooleanField(default=False),
        ),
    ]