# Generated by Django 3.0.6 on 2020-05-29 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200529_0154'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='country',
            unique_together=set(),
        ),
    ]
