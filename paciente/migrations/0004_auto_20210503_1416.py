# Generated by Django 3.1.7 on 2021-05-03 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0003_auto_20210503_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='data_de_diagnostico',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='data_de_nascimento',
            field=models.DateField(null=True),
        ),
    ]