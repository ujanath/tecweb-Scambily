# Generated by Django 4.1 on 2022-08-18 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_prodotto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodotto',
            name='categoria',
            field=models.CharField(choices=[('info', 'informatica'), ('phone', 'telefonia'), ('games', 'console e giochi'), ('book', 'Libri'), ('model', 'modellini')], max_length=5),
        ),
    ]
