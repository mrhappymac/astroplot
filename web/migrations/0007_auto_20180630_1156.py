# Generated by Django 2.0.4 on 2018-06-30 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20180630_0827'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='price',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='price',
            name='coin',
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]
