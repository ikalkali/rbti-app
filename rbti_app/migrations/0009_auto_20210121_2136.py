# Generated by Django 3.1.5 on 2021-01-21 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbti_app', '0008_auto_20210121_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='peminjaman',
            old_name='npm',
            new_name='nim',
        ),
    ]