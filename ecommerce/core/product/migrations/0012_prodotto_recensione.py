# Generated by Django 4.1 on 2022-09-01 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0011_alter_prodotto_stato_articolo_prdotto_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prodotto_recensione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dop', models.DateTimeField(default=django.utils.timezone.now)),
                ('voto', models.DecimalField(choices=[('1', 'pessimo'), ('2', 'discreto'), ('3', 'buono'), ('4', 'molto buono'), ('5', 'perfetto')], decimal_places=1, max_digits=3)),
                ('descrizione', models.CharField(max_length=1000)),
                ('ordine', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.prodotto_ordine')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
