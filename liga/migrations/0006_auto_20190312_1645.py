# Generated by Django 2.1.5 on 2019-03-12 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liga', '0005_player_ftag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='cap',
            field=models.IntegerField(null=True),
        ),
    ]
