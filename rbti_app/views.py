from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.postgres.search import SearchVector
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

class PeminjamanListView(ListView):
    model = Peminjaman
    template_name = 'rbti_app/peminjaman.html'
    context_object_name = 'peminjaman'

    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     data['buku'] = Buku.objects.get.all()

def home_page(request):
    if request.GET.get('param_cari') != '' and request.GET.get('param_cari') is not None :
        param_cari = request.GET.get('param_cari')
        context = {
            'books': Buku.objects.annotate(search=SearchVector('judul', 'penerbit', 'penulis')).filter(search=param_cari).all()
            }
        print(context)
        return render(request, 'rbti_app/newhome.html', context)
    return render(request, 'rbti_app/halaman_depan.html')

    

class BukuListViewCari(ListView):
    model = Buku
    template_name = 'rbti_app/newhome.html'
    context_object_name = 'books'
    ordering = ['id_buku']

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    