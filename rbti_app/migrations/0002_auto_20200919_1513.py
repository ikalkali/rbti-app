# Generated by Django 3.1.1 on 2020-09-19 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbti_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buku',
            name='id_buku',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='buku',
            name='tahun',
            field=models.IntegerField(),
        ),
    ]
