# Generated by Django 2.2.4 on 2020-12-15 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0002_auto_20201215_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_shows',
            name='release_date',
            field=models.DateTimeField(max_length=45),
        ),
    ]