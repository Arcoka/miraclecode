from django.urls import path 
from .import views 

urlpatterns = [ 
    path('', views.berandapenjualan, name='berandapenjualan'),

    
    path('slidepenjualanadmin/', views.slidepenjualanadmin, name='slidepenjualanadmin'),
    path('form-slidepenjualan/', views.formslidepenjualanadmin, name='formslidepenjualanadmin'),
    path('edit-slidepenjualan/<str:token>/', views.editslidepenjualanadmin, name='editslidepenjualanadmin'),
    path('berandapenjualan/delete-slidepenjualan/<str:token>/', views.deleteslidepenjualanadmin, name='deleteslidepenjualanadmin'),

    path('berandapenjualan/pemesananadmin/', views.pemesananadmin, name='pemesananadmin'),
    path('berandapenjualan/form-pemesanan/', views.formpemesananadmin, name='formpemesananadmin'),
    path('berandapenjualan/edit-pemesanan/<str:token>/', views.editpemesananadmin, name='editpemesananadmin'),
    path('berandapenjualan/delete-pemesanan/<str:token>/', views.deletepemesananadmin, name='deletepemesananadmin'),
    

    path('jasaadmin/', views.jasaadmin, name='jasaadmin'),
    path('form-jasa/', views.formjasaadmin, name='formjasaadmin'),
    path('edit-jasa/<str:token>/', views.editjasaadmin, name='editjasaadmin'),
    path('berandapenjualan/delete-jasa/<str:token>/', views.deletejasaadmin, name='deletejasaadmin'),

    
    path('produkadmin/', views.produkadmin, name='produkadmin'),
    path('form-produk/', views.formprodukadmin, name='formprodukadmin'),
    path('edit-produk/<str:token>/', views.editprodukadmin, name='editprodukadmin'),
    path('berandapenjualan/delete-produk/<str:token>/', views.deleteprodukadmin, name='deleteprodukadmin'),
    
    # path('produkadmin/', views.produkadmin, name='produkadmin'),
    # path('berandapenjualan/form-produk/', views.formprodukadmin, name='formprodukadmin'),
    # path('berandapenjualan/edit-produk/<str:token>/', views.editprodukadmin, name='editprodukadmin'),
    # path('berandapenjualan/delete-produk/<str:token>/', views.deleteprodukadmin, name='deleteprodukadmin'),

    path('kategoripenjualanadmin/', views.kategoripenjualanadmin, name='kategoripenjualanadmin'),
    path('form-kategoripenjualan/', views.formkategoripenjualanadmin, name='formkategoripenjualanadmin'),
    path('edit-kategoripenjualan/<str:token>/', views.editkategoripenjualanadmin, name='editkategoripenjualanadmin'),
    path('berandapenjualan/delete-kategoripenjualan/<str:token>/', views.deletekategoripenjualanadmin, name='deletekategoripenjualanadmin'),

    
    path('berandapenjualan/produkadmin/', views.produkadmin, name='produkadmin'),
    path('berandapenjualan/form-produk/', views.formprodukadmin, name='formprodukadmin'),
    path('berandapenjualan/edit-produk/<str:token>/', views.editprodukadmin, name='editprodukadmin'),
    path('berandapenjualan/delete-produk/<str:token>/', views.deleteprodukadmin, name='deleteprodukadmin'),
    ]