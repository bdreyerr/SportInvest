# Generated by Django 3.2 on 2021-04-27 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='num_shares',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='transaction',
            name='trade_choice',
            field=models.CharField(choices=[('1', 'Buy'), ('2', 'Sell')], default=('1', 'Buy'), max_length=300),
            preserve_default=False,
        ),
    ]
