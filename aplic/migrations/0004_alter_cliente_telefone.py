# Generated by Django 4.1.3 on 2022-12-05 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0003_auto_20221205_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=11, verbose_name='Telefone'),
        ),
    ]
