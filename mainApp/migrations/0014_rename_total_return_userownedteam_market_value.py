# Generated by Django 3.2 on 2021-05-04 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0013_transaction_trade_value'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userownedteam',
            old_name='total_return',
            new_name='market_value',
        ),
    ]