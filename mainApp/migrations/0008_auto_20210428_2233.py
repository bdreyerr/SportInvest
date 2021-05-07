# Generated by Django 3.2 on 2021-04-29 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_transaction_trade_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'get_latest_by': 'market_price'},
        ),
        migrations.AlterField(
            model_name='team',
            name='description',
            field=models.TextField(blank=True, max_length=400),
        ),
    ]