from django import forms
from django.forms.formsets import formset_factory
from django.forms import widgets

class PeminjamanForm(forms.Form):
    NIM = forms.CharField(max_length=255)
    Id_Buku = forms.CharField(max_length=255)
    Tanggal_Peminjaman = forms.DateField()