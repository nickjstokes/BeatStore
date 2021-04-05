# Generated by Django 2.2.4 on 2020-12-28 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beat_app', '0002_beat'),
    ]

    operations = [
        migrations.AddField(
            model_name='beat',
            name='iframe_id',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='beat',
            name='likes',
            field=models.ManyToManyField(related_name='liked_beats', to='beat_app.User'),
        ),
    ]