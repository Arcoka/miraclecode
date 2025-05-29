from django.urls import path 
from .import views 
from .views import active_users
from django.contrib import admin
from django.urls import path, include
from .admin_panel import admin_panel_site

urlpatterns = [ 
    path('', views.berandaadmin, name='berandaadmin'),
    path('users/', views.active_users, name='active_users'),
        # Tambahkan URL baru untuk melihat user yang sedang login
    # path('admin/active-users/', active_users, name='active_users'),
    path('admin/', admin.site.urls),
    path('admin_panel/', admin_panel_site.urls),

    path('users/', views.active_users, name='active_users'),
    path('users/add/', views.add_admin_user, name='add_admin_user'),
    path('users/<int:user_id>/edit/', views.edit_admin_user, name='edit_admin_user'),
    path('users/<int:user_id>/delete/', views.delete_admin_user, name='delete_admin_user'),
    
    path('kategori/', views.kategoriadmin, name='kategoriadmin'),
    path('form-kategori/', views.formkategoriadmin, name='formkategoriadmin'),
    path('edit-kategori/<str:token>', views.editkategoriadmin, name='editkategoriadmin'),
    path('delete-kategori/<str:token>', views.deletekategoriadmin, name='deletekategoriadmin'),

    path('berita/', views.beritaadmin, name='beritaadmin'),
    path('form-berita/', views.formberitaadmin, name='formberitaadmin'),
    path('edit-berita/<str:token>', views.editberitaadmin, name='editberitaadmin'),
    path('delete-berita/<str:token>', views.deleteberitaadmin, name='deleteberitaadmin'),

    path('galeri/', views.galeriadmin, name='galeriadmin'),
    path('form-galeri/', views.formgaleriadmin, name='formgaleriadmin'),
    path('edit-galeri/<str:token>', views.editgaleriadmin, name='editgaleriadmin'),
    path('delete-galeri/<str:token>', views.deletegaleriadmin, name='deletegaleriadmin'),

    path('layanan/', views.layananadmin, name='layananadmin'),
    path('form-layanan/', views.formlayananadmin, name='formlayananadmin'),
    path('edit-layanan/<str:token>', views.editlayananadmin, name='editlayananadmin'),
    path('delete-layanan/<str:token>', views.deletelayananadmin, name='deletelayananadmin'),
    
    path('kontak/', views.kontakadmin, name='kontakadmin'),
    path('form-kontak/', views.formkontakadmin, name='formkontakadmin'),
    path('edit-kontak/<str:token>', views.editkontakadmin, name='editkontakadmin'),
    path('delete-kontak/<str:token>', views.deletekontakadmin, name='deletekontakadmin'),

    path('slide/', views.slideadmin, name='slideadmin'),
    path('form-slide/', views.formslideadmin, name='formslideadmin'),
    path('edit-slide/<str:token>', views.editslideadmin, name='editslideadmin'),
    path('delete-slide/<str:token>', views.deleteslideadmin, name='deleteslideadmin'),

    path('bagroundadmin/', views.bagroundadmin, name='bagroundadmin'),
    path('berandapenjualan/form-baground/', views.formbagroundadmin, name='formbagroundadmin'),
    path('berandapenjualan/edit-baground/<str:token>/', views.editbagroundadmin, name='editbagroundadmin'),
    path('berandapenjualan/delete-baground/<str:token>/', views.deletebagroundadmin, name='deletebagroundadmin'),

    path('visimisi/', views.visimisiadmin, name='visimisiadmin'),
    path('form-visimisi/', views.formvisimisiadmin, name='formvisimisiadmin'),
    path('edit-visimisi/<str:token>', views.editvisimisiadmin, name='editvisimisiadmin'),
    path('delete-visimisi/<str:token>', views.deletevisimisiadmin, name='deletevisimisiadmin'),

    path('pekerjaan/', views.pekerjaanadmin, name='pekerjaanadmin'),
    path('form-pekerjaan/', views.formpekerjaanadmin, name='formpekerjaanadmin'),
    path('edit-pekerjaan/<str:token>', views.editpekerjaanadmin, name='editpekerjaanadmin'),
    path('delete-pekerjaan/<str:token>', views.deletepekerjaanadmin, name='deletepekerjaanadmin'),

    path('team/', views.teamadmin, name='teamadmin'),
    path('form-team/', views.formteamadmin, name='formteamadmin'),
    path('edit-team/<str:token>', views.editteamadmin, name='editteamadmin'),
    path('delete-team/<str:token>', views.deleteteamadmin, name='deleteteamadmin'),

    path('modelinkubasi/', views.modelinkubasiadmin, name='modelinkubasiadmin'),
    path('form-modelinkubasi/', views.formmodelinkubasiadmin, name='formmodelinkubasiadmin'),
    path('edit-modelinkubasi/<str:token>', views.editmodelinkubasiadmin, name='editmodelinkubasiadmin'),
    path('delete-modelinkubasi/<str:token>', views.deletemodelinkubasiadmin, name='deletemodelinkubasiadmin'),

    path('testimoni/', views.testimoniadmin, name='testimoniadmin'),
    path('form-testimoni/', views.formtestimoniadmin, name='formtestimoniadmin'),
    path('edit-testimoni/<str:token>', views.edittestimoniadmin, name='edittestimoniadmin'),
    path('delete-testimoni/<str:token>', views.deletetestimoniadmin, name='deletetestimoniadmin'),

    path('profil/', views.profiladmin, name='profiladmin'),
    path('form-profil/', views.formprofiladmin, name='formprofiladmin'),
    path('edit-profil/<str:token>', views.editprofiladmin, name='editprofiladmin'),
    path('delete-profil/<str:token>', views.deleteprofiladmin, name='deleteprofiladmin'),

    path('faq/', views.faqadmin, name='faqadmin'),
    path('form-faq/', views.formfaqadmin, name='formfaqadmin'),
    path('edit-faq/<str:token>', views.editfaqadmin, name='editfaqadmin'),
    path('delete-faq/<str:token>', views.deletefaqadmin, name='deletefaqadmin'),

    path('pesan/', views.pesan_list, name='pesan_list'),
    path('pesan/<slug:slug>/', views.pesan_detail, name='pesan_detail'),
    path('pesan/<slug:slug>/delete/', views.pesan_delete, name='pesan_delete'),
    path('pesan/<slug:slug>/toggle-tampil/', views.toggle_tampil_di_website, name='toggle_tampil_di_website'),

    path('daftartenant/', views.daftartenant_list, name='daftartenant_list'),
    path('daftartenant/<slug:slug>/', views.daftartenant_detail, name='daftartenant_detail'),
    path('daftartenant/<slug:slug>/delete/', views.daftartenant_delete, name='daftartenant_delete'),
    path('daftartenant/<slug:slug>/toggle-tampil/', views.toggle_tampil_di_website, name='toggle_tampil_di_website'),

    # path('daftarlayanan/', views.daftarlayanan_list, name='daftartenant_list'),
    # path('daftarlayanan/<slug:slug>/', views.daftartenant_detail, name='daftartenant_detail'),
    # path('daftarlayanan/<slug:slug>/delete/', views.daftartenant_delete, name='daftartenant_delete'),
    # path('daftarlayanan/<slug:slug>/toggle-tampil/', views.toggle_tampil_di_website, name='toggle_tampil_di_website'),

    path('komentar/', views.komentar_list, name='komentar_list'),
    path('komentar/<slug:slug>/', views.komentar_detail, name='komentar_detail'),
    path('komentar/<slug:slug>/delete/', views.komentar_delete, name='komentar_delete'),
    path('komentar/<slug:slug>/toggle-tampil/', views.toggle_tampil_di_website, name='toggle_tampil_di_website'),

    path('daftarlayanan/', views.admin_daftar_layanan, name='admin_daftar_layanan'),
    path('daftarlayanan/<slug:slug>/', views.admin_detail_layanan, name='admin_detail_layanan'),
    path('daftarlayanan/<slug:slug>/update-status/', views.admin_update_status, name='admin_update_status'),
    
    # path('pesan/', views.pesanadmin, name='pesanadmin'),
    # path('form-pesan/', views.formpesanadmin, name='formpesanadmin'),
    # path('edit-pesan/<str:token>', views.editpesanadmin, name='editpesanadmin'),
    # path('delete-pesan/<str:token>', views.deletepesanadmin, name='deletepesanadmin'),
    ]