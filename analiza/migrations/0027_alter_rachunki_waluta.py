# Generated by Django 3.2.6 on 2021-09-01 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analiza', '0026_auto_20210827_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rachunki',
            name='waluta',
            field=models.CharField(choices=[('PLN', 'PLN'), ('EUR', 'EUR')], default='', max_length=4),
        ),
    ]