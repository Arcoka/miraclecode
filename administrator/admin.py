from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils.timezone import now
import json
from .models import Kategori, Berita, Kontak, Pesan, Komentar, Profil, Slide, Galeri, Layanan, Baground, VisiMisi, Pekerjaan, Team, ModelInkubasi, Testimoni, Faq, DaftarTenant, DaftarLayanan
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import MenuPilihan, AdminPanelUser
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q


# class ActiveUserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'last_login')

#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         return qs.filter(is_active=True)  # Hanya user aktif yang ditampilkan

# admin.site.unregister(User)
# admin.site.register(User, ActiveUserAdmin)

def create_admin_groups():
    # Buat grup Admin dan Superadmin jika belum ada
    admin_group, created = Group.objects.get_or_create(name='Admin')
    superadmin_group, created = Group.objects.get_or_create(name='Superadmin')
    
    # Reset permissions
    admin_group.permissions.clear()
    superadmin_group.permissions.clear()
    
    # Dapatkan content type untuk model yang relevan
    menu_pilihan_ct = ContentType.objects.get(app_label='yourapp', model='menupilihan')
    user_ct = ContentType.objects.get(app_label='auth', model='user')
    adminpaneluser_ct = ContentType.objects.get(app_label='yourapp', model='adminpaneluser')
    
    # Tetapkan izin untuk Admin (hanya bisa mengelola MenuPilihan)
    menu_permissions = Permission.objects.filter(
        content_type=menu_pilihan_ct,
        codename__in=['add_menupilihan', 'change_menupilihan', 'view_menupilihan']
    )
    admin_group.permissions.add(*menu_permissions)
    
    # Tetapkan izin untuk Superadmin (bisa mengelola semua termasuk User dan AdminPanelUser)
    # Izin untuk MenuPilihan
    all_menu_permissions = Permission.objects.filter(content_type=menu_pilihan_ct)
    
    # Izin untuk User
    user_permissions = Permission.objects.filter(content_type=user_ct)
    
    # Izin untuk AdminPanelUser
    adminpaneluser_permissions = Permission.objects.filter(content_type=adminpaneluser_ct)
    
    # Gabungkan semua izin
    all_permissions = list(all_menu_permissions) + list(user_permissions) + list(adminpaneluser_permissions)
    superadmin_group.permissions.add(*all_permissions)
    
    return admin_group, superadmin_group

# Admin untuk MenuPilihan
@admin.register(MenuPilihan)
class MenuPilihanAdmin(admin.ModelAdmin):
    list_display = ['nama', 'deskripsi', 'aktif']
    search_fields = ['nama']
    list_filter = ['aktif']

# Admin untuk AdminPanelUser
class AdminPanelUserInline(admin.StackedInline):
    model = AdminPanelUser
    can_delete = False
    verbose_name_plural = 'Admin Panel Profile'

# Ubah admin User bawaan untuk menampilkan AdminPanelUser
class CustomUserAdmin(BaseUserAdmin):
    inlines = [AdminPanelUserInline]
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_admin_panel_superadmin']
    
    def is_admin_panel_superadmin(self, obj):
        try:
            return obj.admin_panel_profile.is_superadmin
        except AdminPanelUser.DoesNotExist:
            return False
    
    is_admin_panel_superadmin.short_description = 'Superadmin'
    is_admin_panel_superadmin.boolean = True

# Unregister User bawaan dan register dengan CustomUserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display=('id', 'nama', 'aktif')
    prepopulated_fields = {"slug": ("nama",)} #membuat slug otomatis

@admin.register(Berita)
class BeritaAdmin(admin.ModelAdmin):
    list_display = ('id', 'judul', 'kategori', 'tanggal_upload')
    prepopulated_fields = {"slug": ("judul",)}
    list_filter = ('kategori', 'tanggal_upload')

@admin.register(Kontak)
class KontakAdmin(admin.ModelAdmin):
    list_display=('id', 'alamat', "no_1","no_2","email","hari","jam")
    prepopulated_fields = {"slug": ("email",)}


@admin.register(Pesan)
class PesanAdmin(admin.ModelAdmin):
    list_display = ('nama', 'email', 'tanggal_upload', 'is_read', 'aktif')
    list_filter = ('is_read', 'aktif', 'tanggal_upload')
    search_fields = ('nama', 'email', 'pesan')
    readonly_fields = ('tanggal_upload', 'token_pesan', 'slug')
    date_hierarchy = 'tanggal_upload'
    
    actions = ['mark_as_read', 'mark_as_unread']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Tandai pesan terpilih sebagai sudah dibaca"
    
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Tandai pesan terpilih sebagai belum dibaca"

try:
    admin.site.register(Pesan, PesanAdmin)
except admin.sites.AlreadyRegistered:
    pass

@admin.register(Komentar)
class KomentarAdmin(admin.ModelAdmin):
    list_display = ('nama', 'email', 'tanggal_upload', 'is_read', 'aktif')
    list_filter = ('is_read', 'aktif', 'tanggal_upload')
    search_fields = ('nama', 'email', 'komentar')
    readonly_fields = ('tanggal_upload', 'token_komentar', 'slug')
    date_hierarchy = 'tanggal_upload'
    
    actions = ['mark_as_read', 'mark_as_unread']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Tandai komentar terpilih sebagai sudah dibaca"
    
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Tandai komentar terpilih sebagai belum dibaca"

try:
    admin.site.register(Komentar, KomentarAdmin)
except admin.sites.AlreadyRegistered:
    pass


@admin.register(DaftarTenant)
class DaftarTenantAdmin(admin.ModelAdmin):
    list_display = ('nama', 'email', 'tanggal_upload', 'is_read', 'aktif')
    list_filter = ('is_read', 'aktif', 'tanggal_upload')
    search_fields = ('nama', 'email', 'daftartenant')
    readonly_fields = ('tanggal_upload', 'token_daftartenant', 'slug')
    date_hierarchy = 'tanggal_upload'
    
    actions = ['mark_as_read', 'mark_as_unread']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Tandai daftartenant terpilih sebagai sudah dibaca"
    
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Tandai daftartenant terpilih sebagai belum dibaca"

try:
    admin.site.register(DaftarTenant, DaftarTenantAdmin)
except admin.sites.AlreadyRegistered:
    pass


@admin.register(DaftarLayanan)
class DaftarLayananAdmin(admin.ModelAdmin):
    list_display = ['nama', 'email', 'telepon', 'jenislayanan', 'jenisproduk', 'waktu', 'is_read', 'tanggal_upload', 'aktif']
    list_filter = ['is_read', 'aktif', 'jenislayanan', 'jenisproduk']
    search_fields = ['nama', 'email', 'telepon']
    date_hierarchy = 'tanggal_upload'
    readonly_fields = ['token_daftarlayanan', 'tanggal_upload', 'slug']
    fieldsets = (
        ('Informasi Pelanggan', {
            'fields': ('nama', 'email', 'alamat', 'telepon')
        }),
        ('Detail Layanan', {
            'fields': ('jenislayanan', 'jenisproduk', 'waktu', 'pesan')
        }),
        ('Status', {
            'fields': ('is_read', 'aktif')
        }),
        ('Informasi Sistem', {
            'fields': ('token_daftarlayanan', 'tanggal_upload', 'slug'),
            'classes': ('collapse',)
        }),
    )
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Tandai sebagai sudah dibaca"
    
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Tandai sebagai belum dibaca"
    
    actions = ['mark_as_read', 'mark_as_unread']
    
    def get_ordering(self, request):
        return ['-tanggal_upload']

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display=('id', 'judul', 'deskripsi','gambar', 'gambar_2')
    prepopulated_fields = {"slug": ("judul",)}

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display=('id', 'nama', 'teks_awal', 'teks_dua','gambar_slide')
    prepopulated_fields = {"slug": ("nama",)}

@admin.register(Baground)
class BagroundAdmin(admin.ModelAdmin):
    list_display=('id', 'nama_baground', 'gambar_baground')
    prepopulated_fields = {"slug": ("nama_baground",)}

@admin.register(VisiMisi)
class VisiMisiAdmin(admin.ModelAdmin):
    list_display=('id', 'visi','misi', 'sasaran','tujuan')
    prepopulated_fields = {"slug": ("visi",)}

@admin.register(Galeri)
class GaleriAdmin(admin.ModelAdmin):
    list_display=('id', 'nama_galeri', 'aktif', 'gambar_galeri')
    prepopulated_fields = {"slug": ("nama_galeri",)}

@admin.register(Layanan)
class LayananAdmin(admin.ModelAdmin):
    list_display=('id', 'nama', 'isi')
    prepopulated_fields = {"slug": ("nama",)}

@admin.register(Pekerjaan)
class PekerjaanAdmin(admin.ModelAdmin):
    list_display=('id', 'nama', 'aktif', 'isi', 'gambar')
    prepopulated_fields = {"slug": ("nama",)}

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=('id', 'gambar', 'nama','jabatan', 'facebook', 'twitter', 'instagram', 'aktif')
    prepopulated_fields = {"slug": ("nama",)}
    
@admin.register(Testimoni)
class TestimoniAdmin(admin.ModelAdmin):
    list_display=('id', 'deskripsi', 'gambar', 'nama','jabatan', 'aktif')
    prepopulated_fields = {"slug": ("nama",)}


@admin.register(ModelInkubasi)
class ModelInkubasiAdmin(admin.ModelAdmin):
    list_display=('id', 'nama', 'gambar', 'deskripsi', 'aktif')
    prepopulated_fields = {"slug": ("nama",)}

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display=('id', 'noslug', 'tanya', 'jawab', 'aktif')
    prepopulated_fields = {"slug": ("noslug",)}




