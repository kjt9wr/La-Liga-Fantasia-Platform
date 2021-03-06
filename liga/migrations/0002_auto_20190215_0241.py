# Generated by Django 2.1.5 on 2019-02-15 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('position', models.CharField(max_length=3)),
                ('kept', models.BooleanField()),
            ],
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='Cap',
            new_name='cap',
        ),
    ]
