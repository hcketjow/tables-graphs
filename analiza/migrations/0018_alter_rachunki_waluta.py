# Generated by Django 3.2.6 on 2021-08-27 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analiza', '0017_alter_rachunki_waluta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rachunki',
            name='waluta',
            field=models.CharField(choices=[('EUR', 'EUR'), ('PLN', 'PLN')], default='', max_length=4),
        ),
    ]
