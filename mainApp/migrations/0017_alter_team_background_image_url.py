# Generated by Django 3.2 on 2021-05-04 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0016_team_background_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='background_image_url',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
