from django.db import models
from django.shortcuts import reverse


class Buku(models.Model):
    id_buku = models.CharField(max_length=255, primary_key=True)
    judul = models.CharField(max_length=255)
    penulis = models.CharField(max_length=255)
    penerbit = models.CharField(max_length=255)
    tahun = models.CharField(max_length=255)

    def __str__(self):
        return self.id_buku


class Mahasiswa(models.Model):
    nim = models.BigIntegerField(primary_key=True)
    nama = models.CharField(null=False, max_length=255)
    email = models.EmailField(null=False, max_length=255, default=None)

    def __str__(self):
        return self.nama


class Peminjaman(models.Model):
    tanggal_peminjaman = models.DateField(auto_now_add=True)
    tanggal_pengembalian = models.DateField(null=True)
    nim = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    id_buku = models.ForeignKey(Buku, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('rbti_app:home')

# class Admin(models.Model):
#     username = models.Charfield(max_length=255, primary_key = True)
#     password = models.CharField(max_length=255)
