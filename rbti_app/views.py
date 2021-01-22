from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from .models import (Buku, Mahasiswa, Peminjaman)
from .forms import PeminjamanForm
from django.db import connection, DatabaseError, transaction
from django.utils import timezone
# Create your views here.


class BukuListView(ListView):
    model = Buku
    template_name = 'rbti_app/newhome.html'
    context_object_name = 'books'
    ordering = ['id_buku']


class BukuAvailableListView(ListView):
    model = Buku
    template_name = 'rbti_app/newhome.html'
    context_object_name = 'books'
    ordering = ['id_buku']

    def get_queryset(self):
        id_buku_dipinjam = get_object_or_404(
            Peminjaman, self.kwargs.get(id_buku_id='id_buku_id'))
        return Buku.objects.filter(id_buku=id_buku_dipinjam)


class BukuListViewAlt(ListView):
    model = Buku
    template_name = 'rbti_app/home.html'
    context_object_name = 'books'
    ordering = ['id_buku']


class MahasiswaListView(ListView):
    model = Mahasiswa
    template_name = 'rbti_app/mahasiswa.html'
    context_object_name = 'mahasiswa'
    ordering = 'nama'


class PeminjamanCreateView(CreateView):
    model = Peminjaman
    fields = ["nim"]

    def dispatch(self, request, *args, **kwargs):
        self.id_buku_id = get_object_or_404(Buku, pk=kwargs['id_buku'])
        print("!!!!!!!!!!!! ID BUKU ADALAH {idbuku} !!!!!!!!!!!!! ".format(
            idbuku=self.id_buku_id))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.id_buku_id = self.id_buku_id
        form.instance.tanggal_peminjaman = timezone.now()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        data = super(PeminjamanCreateView, self).get_context_data(**kwargs)
        data['id_buku'] = Buku.objects.get(pk=self.id_buku_id)
        data['judul'] = Buku.objects.get(pk=self.id_buku_id).judul
        data['penerbit'] = Buku.objects.get(pk=self.id_buku_id).penerbit
        data['tahun'] = Buku.objects.get(pk=self.id_buku_id).tahun
        return data

        # self.id_buku_id = get_object_or_404(Buku, pk=kwargs['id_buku'])
