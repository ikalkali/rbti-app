# Generated by Django 3.1.3 on 2020-11-16 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbti_app', '0003_auto_20200919_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('npm', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Peminjaman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_peminjaman', models.DateField(auto_now_add=True)),
                ('tanggal_pengembalian', models.DateField(null=True)),
                ('id_buku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbti_app.buku')),
                ('id_mahasiswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbti_app.mahasiswa')),
            ],
        ),
    ]
