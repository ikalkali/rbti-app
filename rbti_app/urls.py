from django.urls import path
from .views import (
    BukuListView,
    BukuListViewAlt,
    BukuAvailableListView,
    MahasiswaListView,
    PeminjamanCreateView,
    PeminjamanListView,
    BukuListViewCari,
    home_page
)
app_name = "rbti_app"
urlpatterns = [
    path('', home_page, name='home'),
    path('semua-buku/', BukuListView.as_view(), name='semua-buku'),
    path('available/', BukuAvailableListView.as_view(), name='home-available'),
    path('mahasiswa/', MahasiswaListView.as_view(), name='mahasiswa'),
    path('alt/', BukuListViewAlt.as_view(), name='home-alt'),
    path('peminjaman/', PeminjamanListView.as_view(), name='peminjaman'),
    path('peminjaman/<int:id_buku>/',
         PeminjamanCreateView.as_view(), name="peminjaman"),
]
