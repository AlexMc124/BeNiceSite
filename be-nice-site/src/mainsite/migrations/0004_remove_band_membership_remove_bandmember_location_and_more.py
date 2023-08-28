# Generated by Django 4.2.1 on 2023-07-23 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_make_defaults_for_choices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='membership',
        ),
        migrations.RemoveField(
            model_name='bandmember',
            name='location',
        ),
        migrations.AddField(
            model_name='band',
            name='location',
            field=models.ManyToManyField(to='mainsite.location'),
        ),
    ]