# Generated by Django 2.1.5 on 2019-03-12 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liga', '0006_auto_20190312_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='cap',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
