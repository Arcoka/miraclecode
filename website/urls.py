from django.urls import path 
from .import views 
from .views import login_view, logout_view, berita_list, berita_detail, hubungi_kami, komentar_pelanggan, faq, produk_detail

  # Pastikan ini ada

urlpatterns = [ 
    path('', views.beranda, name='home'), 
    path('penjualan', views.berandapenjualan, name='penjualan'),
    path('produk_detail/<slug:slug>/', views.produk_detail, name='produk_detail'),
    # path('slide', views.beranda, name='slide'),
    # path('study', views.beranda, name='study'),
    path('visimisi', views.visimisi, name='visimisi'),
    path('profil/', views.profil, name='profil'),
    path('faq/', views.faq, name='faq'), 
    path('berita/<slug:slug>/', berita_detail, name='berita_detail'),
    path('beritalist/', views.berita_list, name='berita_list'),
    path('hubungi-kami/', views.hubungi_kami, name='hubungi_kami'),
    path('kontak/', views.kontak, name='kontak'),
    path('komentar-pelanggan/', views.komentar_pelanggan, name='komentar_pelanggan'),
    path('daftar-tenant/', views.daftar_tenant, name='daftar_tenant'),
    path('layanan/', views.layanan, name='layanan'),
    path('modelinkubasi/', views.modelinkubasi, name='modelinkubasi'),
    path('seleksi/', views.seleksi, name='seleksi'),
    path('tenantinkubator/', views.tenantinkubator, name='tenantinkubator'),
    path('toggle-aktif/<int:id>/', views.toggle_aktif, name='toggle_aktif'),
    path('baground/', views.baground, name='baground'),
    path('sejarah/', views.sejarah, name='sejarah'),
    path('daftar-layanan/', views.submit_layanan, name='submit_layanan'),
    path('jenislayanan/', views.jenislayanan, name='jenislayanan'),
    path('konfirmasi-layanan/<slug:slug>/', views.konfirmasi_layanan, name='konfirmasi_layanan'),
    path('cek-status-layanan/', views.cek_status_layanan, name='cek_status_layanan'),
    
    # path('daftar-tenant/sukses/', views.daftar_tenant_sukses, name='daftar_tenant_sukses'),
    # path('hubungi-kami/', views.hubungi_kami, name='hubungi_kami'),
    # path('success/', views.success_page, name='success_page'),
    # path('berita/<slug:berita_slug>/', views.detail_berita, name='detail_berita'),
    # path('kategori', views.berita, name='news'),
    # path('kontak', views.kontak, name='contact'), 


    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),  # Tambahkan URL logout

    
    
    
    ]