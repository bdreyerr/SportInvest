# Generated by Django 3.2 on 2021-05-04 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0015_userownedteam_total_return'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='background_image_url',
            field=models.CharField(default='None', max_length=50),
        ),
    ]