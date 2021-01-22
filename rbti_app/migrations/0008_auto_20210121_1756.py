# Generated by Django 3.1.5 on 2021-01-21 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbti_app', '0007_mahasiswa_peminjaman'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mahasiswa',
            old_name='npm',
            new_name='nim',
        ),
        migrations.AddField(
            model_name='mahasiswa',
            name='email',
            field=models.EmailField(default=None, max_length=255),
        ),
    ]
