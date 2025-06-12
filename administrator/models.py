from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
import uuid
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.utils.translation import gettext_lazy as _


# Model untuk menu yang akan dikelola oleh admin biasa
class MenuPilihan(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True, null=True)
    aktif = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name = 'Menu Pilihan'
        verbose_name_plural = 'Menu Pilihan'

# Model Admin Panel User (memperluas User bawaan)
class AdminPanelUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_panel_profile')
    is_superadmin = models.BooleanField(default=False, verbose_name=_('Super Admin'))
    
    def __str__(self):
        return f"{self.user.username} - {'Superadmin' if self.is_superadmin else 'Admin'}"
    
    class Meta:
        verbose_name = 'Admin Panel User'
        verbose_name_plural = 'Admin Panel Users'


class Kategori(models.Model):
    nama = models.CharField(max_length=200, blank=True, null=True)
    aktif = models.BooleanField(default= True)
    token_kategori = models.CharField(max_length=300,  blank=True, null=True)
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    class Meta:
        verbose_name_plural = 'Data Kategori'

    def __str__(self): 
        return self.nama

    def save(self, *args, **kwargs):  # new 
        if not self.slug: 
            self.slug = slugify(self.nama) 
        return super().save(*args, **kwargs) 


class Berita(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)  # Pakai ForeignKey ke Kategori
    judul = models.CharField(max_length=300)
    gambar = models.ImageField(upload_to='gambar/berita/', blank=True, null=True)
    deskripsi = RichTextField( blank=True, null=True)
    isi_berita = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    token_berita = models.CharField(max_length=300,  blank=True, null=True)
    tanggal_upload = models.DateTimeField(default=timezone.now)  

    class Meta:
        verbose_name_plural = 'Data Berita'
        ordering = ['-tanggal_upload']  # Mengurutkan dari yang terbaru

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.judul)
        super().save(*args, **kwargs)

class Slide(models.Model):
    nama = models.CharField(max_length=200, blank=True, null=True)
    teks_awal = models.CharField(max_length=200, blank=True, null=True)
    teks_dua = models.CharField(max_length=200, blank=True, null=True)
    # teks_tiga = models.CharField(max_length=200, blank=True, null=True)
    gambar_slide = models.ImageField(upload_to='gambar/slide', blank=False, null=True)
    aktif = models.BooleanField(default=True)
    token_slide = models.CharField(max_length=300,  blank=True, null=True)
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    class Meta:
        verbose_name_plural = 'Data Slide'

class Baground(models.Model):
    nama_baground = RichTextField(max_length=200, blank=True, null=True)
    gambar_baground = models.ImageField(upload_to='gambar/baground', blank=False, null=True)
    aktif = models.BooleanField(default=True)
    token_baground = models.CharField(max_length=300,  blank=True, null=True)
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    class Meta:
        verbose_name_plural = 'Data Baground'

    def save(self, *args, **kwargs):  # new 
        if not self.slug: 
            self.slug = slugify(self.nama_baground) 
        return super().save(*args, **kwargs) 

class VisiMisi(models.Model):
    visi = RichTextField(max_length=200, blank=True, null=True)
    misi = RichTextField(max_length=200, blank=True, null=True)
    sasaran = RichTextField(max_length=200, blank=True, null=True)
    tujuan = RichTextField(max_length=200, blank=True, null=True)
    aktif = models.BooleanField(default=True)
    token_visimisi = models.CharField(max_length=300, blank=True, null=True)
    tanggal_upload = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True)
    
    class Meta:
        verbose_name_plural = 'Data VisiMisi'

    def save(self, *args, **kwargs):
        if not self.slug:
            # Coba buat slug dari field yang ada (visi, misi, sasaran, tujuan)
            base_text = None
            
            # Prioritas: visi -> misi -> sasaran -> tujuan -> fallback
            if self.visi:
                base_text = self.visi
            elif self.misi:
                base_text = self.misi
            elif self.sasaran:
                base_text = self.sasaran
            elif self.tujuan:
                base_text = self.tujuan
            
            if base_text:
                # Bersihkan HTML tags dan ambil 50 karakter pertama
                import re
                clean_text = re.sub(r'<[^>]*>', '', str(base_text))
                base_slug = slugify(clean_text[:50])
            else:
                # Fallback jika semua field kosong
                base_slug = f"visimisi-{uuid.uuid4().hex[:8]}"
            
            # Pastikan slug unik
            slug = base_slug
            counter = 1
            
            while VisiMisi.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            
            self.slug = slug
        
        return super().save(*args, **kwargs)
    
class Kontak(models.Model):
    alamat = models.CharField(max_length=100,blank=True, null=True)
    no_1 = models.CharField(max_length=20, null=True)
    no_2 = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    hari = models.CharField(max_length=100)  # contoh: "Sabtu - Kamis"
    jam = models.CharField(max_length=100)  # contoh: "09:00AM - 04:00PM"
    token_kontak = models.CharField(max_length=300,  blank=True, null=True)
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    aktif = models.BooleanField(default=True)
    def save(self, *args, **kwargs):  # new 
        if not self.slug: 
            self.slug = slugify(self.email) 
        return super().save(*args, **kwargs) 
    
    class Meta:
        verbose_name_plural = "Informasi Kontak"

class Pesan(models.Model):
    nama = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    pesan = models.TextField(blank=True, null=True)
    is_read = models.BooleanField(default=False)
    token_pesan = models.CharField(max_length=300, blank=True, null=True)
    tanggal_upload = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True)
    aktif = models.BooleanField(default=True)

    tampil_di_website = models.BooleanField(default=False, 
                        verbose_name="Tampilkan di Website")
    def __str__(self):
        return f"Pesan dari {self.nama} ({self.tanggal_upload.strftime('%Y-%m-%d')})"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.nama)
            timestamp = timezone.now().strftime("%Y%m%d%H%M%S%f")
            unique_id = str(uuid.uuid4())[:8]
            self.slug = f"{base_slug}-{timestamp}-{unique_id}"

            # Ensure slug is unique
            original_slug = self.slug
            num = 1
            while Pesan.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{num}"
                num += 1

        if not self.token_pesan:
            self.token_pesan = str(uuid.uuid4())
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Pesan"
        verbose_name_plural = "Pesan"

class DaftarTenant(models.Model):
    nama = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telepon = models.CharField(max_length=20, blank=True, null=True)  # Fixed: Changed from EmailField to CharField
    namausaha = models.CharField(max_length=200, blank=True, null=True)  # Fixed: Changed from TextField for consistency
    jenisusaha = models.CharField(max_length=200, blank=True, null=True)  # Fixed: Changed from TextField for consistency
    is_read = models.BooleanField(default=False)
    token_daftartenant = models.CharField(max_length=300, blank=True, null=True)
    tanggal_upload = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True)
    aktif = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nama} - {self.namausaha}" if self.nama and self.namausaha else "Tenant"

class DaftarLayanan(models.Model):
    JENIS_LAYANAN_CHOICES = (
        ('konsultasi', 'Konsultasi'),
        ('pemasangan', 'Pemasangan'),
        ('perbaikan', 'Perbaikan'),
        ('lainnya', 'Lainnya'),
    )
    
    JENIS_PRODUK_CHOICES = (
        ('produk_a', 'Produk A'),
        ('produk_b', 'Produk B'),
        ('produk_c', 'Produk C'),
        ('lainnya', 'Lainnya'),
    )

    nama = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nama Lengkap")
    email = models.EmailField(max_length=100, blank=True, null=True, verbose_name="Email")
    alamat = models.TextField(blank=True, null=True, verbose_name="Alamat")
    telepon = models.CharField(max_length=20, blank=True, null=True, verbose_name="Nomor Telepon")
    jenislayanan = models.CharField(max_length=20, choices=JENIS_LAYANAN_CHOICES, blank=True, null=True, verbose_name="Jenis Layanan")
    jenisproduk = models.CharField(max_length=20, choices=JENIS_PRODUK_CHOICES, blank=True, null=True, verbose_name="Jenis Produk")
    waktu = models.DateTimeField(blank=True, null=True, verbose_name="Waktu Layanan")
    pesan = models.TextField(blank=True, null=True, verbose_name="Pesan")
    is_read = models.BooleanField(default=False, verbose_name="Sudah Dibaca")
    token_daftarlayanan = models.CharField(max_length=300, blank=True, null=True, editable=False)
    tanggal_upload = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Tanggal Permintaan")
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True)
    aktif = models.BooleanField(default=True, verbose_name="Aktif")
    
    class Meta:
        verbose_name = "Daftar Layanan"
        verbose_name_plural = "Daftar Layanan"
    
    def save(self, *args, **kwargs):
        if not self.token_daftarlayanan:
            self.token_daftarlayanan = str(uuid.uuid4())
        
        if not self.slug:
            base_slug = slugify(self.nama) if self.nama else "layanan"
            slug = base_slug
            counter = 1
            
            # Check if slug exists
            while DaftarLayanan.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            
            self.slug = slug
            
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.nama}" if self.nama else "Layanan Tanpa Nama"

class Komentar(models.Model):
    nama = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    komentar = models.TextField(blank=True, null=True)
    is_read = models.BooleanField(default=False)
    token_komentar = models.CharField(max_length=300, blank=True, null=True)
    tanggal_upload = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True)
    aktif = models.BooleanField(default=True)

    tampil_di_website = models.BooleanField(default=False, 
                        verbose_name="Tampilkan di Website")

    def __str__(self):
        return f"Komentar dari {self.nama} ({self.tanggal_upload.strftime('%Y-%m-%d')})"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.nama)
            timestamp = timezone.now().strftime("%Y%m%d%H%M%S%f")
            unique_id = str(uuid.uuid4())[:8]
            self.slug = f"{base_slug}-{timestamp}-{unique_id}"

            # Ensure slug is unique
            original_slug = self.slug
            num = 1
            while Komentar.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{num}"
                num += 1

        if not self.token_komentar:
            self.token_komentar = str(uuid.uuid4())
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Komentar"
        verbose_name_plural = "Komentar"
        
class Profil(models.Model):
    judul = models.CharField(max_length=200, blank=False, null=True)
    deskripsi = RichTextField(max_length=600, blank=True, null=True)
    gambar = models.ImageField(upload_to='gambar', blank=False, null=True, verbose_name="Gambar (1920 x 1200 pixel)")
    gambar_2 = models.ImageField(upload_to='gambar', blank=False, null=True, verbose_name="Gambar (1920 x 1200 pixel)")
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    aktif = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    token_profil= models.CharField(max_length=300,  blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Data Profil'

    def save(self, *args, **kwargs):  # new 
        if not self.slug: 
            self.slug = slugify(self.judul) 
        return super().save(*args, **kwargs) 
    
class Sejarah(models.Model):
    judul = models.CharField(max_length=200, blank=False, null=True)
    isi = models.CharField(max_length=200, blank=False, null=True)
    detail = models.CharField(max_length=200, blank=False, null=True)
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    aktif = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    token_sejarah= models.CharField(max_length=300,  blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Data Sejarah'

    def save(self, *args, **kwargs):  # new 
        if not self.slug: 
            self.slug = slugify(self.judul) 
        return super().save(*args, **kwargs) 

class Galeri(models.Model):
    nama_galeri = models.CharField(max_length=200, blank=True, null=True)
    gambar_galeri = models.ImageField(upload_to='gambar', blank=False, null=True)
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    token_galeri = models.CharField(max_length=300,  blank=True, null=True)
    aktif = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = 'Data Galeri'

    def save(self, *args, **kwargs):  # new 
        if not self.slug: 
            self.slug = slugify(self.nama_galeri) 
        return super().save(*args, **kwargs) 

class Layanan(models.Model):
    nama = models.CharField(max_length=200, blank=True, null=True)
    isi = RichTextField(blank=True, null=True) #RichTextField menambah ck editor ke pengeditan admin
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    token_layanan = models.CharField(max_length=300,  blank=True, null=True)
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        verbose_name_plural = 'Data Layanan'

    def save(self, *args, **kwargs):  # new 
        if not self.slug: 
            self.slug = slugify(self.nama) 
        return super().save(*args, **kwargs) 

class Pekerjaan(models.Model):
    judul = models.CharField(max_length=200, blank=True, null=True)
    teks = models.CharField(max_length=200, blank=True, null=True)
    gambar = models.ImageField(upload_to='gambar', blank=False, null=True)
    nama = models.CharField(max_length=200, blank=True, null=True)
    isi = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    token_pekerjaan = models.CharField(max_length=300,  blank=True, null=True)
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    aktif = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = 'Data Pekerjaan'

    def save(self, *args, **kwargs):  # new 
        if not self.slug: 
            self.slug = slugify(self.nama) 
        return super().save(*args, **kwargs) 

class Team(models.Model):
    gambar = models.ImageField(upload_to='gambar', blank=False, null=True)
    nama = models.CharField(max_length=200, blank=True, null=True)
    jabatan = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    token_team = models.CharField(max_length=300,  blank=True, null=True)
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    aktif = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = 'Data Team'

    def save(self, *args, **kwargs):  # new 
        if not self.slug: 
            self.slug = slugify(self.nama) 
        return super().save(*args, **kwargs) 

class ModelInkubasi(models.Model):
    nama = models.CharField(max_length=200, blank=True, null=True)
    gambar = models.ImageField(upload_to='gambar', blank=False, null=True)
    deskripsi = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    token_modelinkubasi = models.CharField(max_length=300,  blank=True, null=True)
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    aktif = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = 'Data Model Inkubasi'

    def save(self, *args, **kwargs):  # new 
        if not self.slug: 
            self.slug = slugify(self.nama) 
        return super().save(*args, **kwargs) 

class Testimoni(models.Model):
    deskripsi = RichTextField(blank=True, null=True)
    gambar = models.ImageField(upload_to='gambar', blank=False, null=True)
    nama = models.CharField(max_length=200, blank=True, null=True)
    jabatan = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    token_testimoni = models.CharField(max_length=300,  blank=True, null=True)
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    aktif = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = 'Data Testimoni'

    def save(self, *args, **kwargs):  # new 
        if not self.slug: 
            self.slug = slugify(self.nama) 
        return super().save(*args, **kwargs) 


class Faq(models.Model):
    tanya = models.CharField(max_length=1000, blank=True, null=True)
    jawab = models.CharField(max_length=1000, blank=True, null=True)
    noslug = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    token_faq = models.CharField(max_length=300,  blank=True, null=True)
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    aktif = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = 'Data Faq'

    def save(self, *args, **kwargs):  # new 
        if not self.slug: 
            self.slug = slugify(self.noslug) 
        return super().save(*args, **kwargs) 

class JenisLayanan(models.Model):
    judul = models.CharField(max_length=1000, blank=True, null=True)
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    token_faq = models.CharField(max_length=300,  blank=True, null=True)
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    aktif = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = 'Data Faq'

    def save(self, *args, **kwargs):  # new 
        if not self.slug: 
            self.slug = slugify(self.noslug) 
        return super().save(*args, **kwargs) 
    
class Seleksi(models.Model):
    judul = models.CharField(max_length=1000, blank=True, null=True)
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    token_faq = models.CharField(max_length=300,  blank=True, null=True)
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    aktif = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = 'Data Faq'

    def save(self, *args, **kwargs):  # new 
        if not self.slug: 
            self.slug = slugify(self.noslug) 
        return super().save(*args, **kwargs) 
    
class TenantInkubator(models.Model):
    judul = models.CharField(max_length=1000, blank=True, null=True)
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    token_faq = models.CharField(max_length=300,  blank=True, null=True)
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    aktif = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = 'Data Faq'

    def save(self, *args, **kwargs):  # new 
        if not self.slug: 
            self.slug = slugify(self.noslug) 
        return super().save(*args, **kwargs) 
