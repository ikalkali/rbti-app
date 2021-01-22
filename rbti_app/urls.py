from django.urls import path
from .views import (
    BukuListView,
    BukuListViewAlt,
    BukuAvailableListView,
    MahasiswaListView,
    PeminjamanCreateView,
)
app_name = "rbti_app"
urlpatterns = [
    path('', BukuListView.as_view(), name='home'),
    path('available/', BukuAvailableListView.as_view(), name='home-available'),
    path('mahasiswa/', MahasiswaListView.as_view(), name='mahasiswa'),
    path('alt/', BukuListViewAlt.as_view(), name='home-alt'),
    path('peminjaman/<int:id_buku>/',
         PeminjamanCreateView.as_view(), name="peminjaman"),
]
