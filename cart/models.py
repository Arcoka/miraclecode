from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify 

class Cart(models.Model):
    user = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"{self.user} - {self.product}"

class SlidePenjualan(models.Model):
    
    deskripsi = RichTextField(max_length=200, blank=True, null=True)
    judul = models.CharField(max_length=200, blank=True, null=True)
    gambar = models.ImageField(upload_to='gambar/slide', blank=False, null=True)
    aktif = models.BooleanField(default=True)
    token_slidepenjualan = models.CharField(max_length=300,  blank=True, null=True)
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    class Meta:
        verbose_name_plural = 'Data SlidePenjualan'


class Pemesanan(models.Model):
    no_pemesanan = models.CharField(max_length=200, blank=True, null=True)
    nama_pemesanan = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    token_pemesanan = models.CharField(max_length=300,  blank=True, null=True)
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    aktif = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = 'Data Pemesanan'

    def save(self, *args, **kwargs):  # new 
        if not self.slug: 
            self.slug = slugify(self.nama_pemesanan) 
        return super().save(*args, **kwargs) 

class Jasa(models.Model):
    slugkata = models.CharField(max_length=200, blank=True, null=True)
    deskripsi = models.CharField(max_length=200, blank=True, null=True)
    gambar = models.ImageField(upload_to='gambar', blank=False, null=True)
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    token_jasa = models.CharField(max_length=300,  blank=True, null=True)
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    aktif = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = 'Data Jasa'

    def save(self, *args, **kwargs):  # new 
        if not self.slug: 
            self.slug = slugify(self.slugkata) 
        return super().save(*args, **kwargs)

class KategoriPenjualan(models.Model):
    nama = models.CharField(max_length=200, blank=True, null=True)
    filter = models.CharField(max_length=200, blank=True, null=True)
    aktif = models.BooleanField(default=True)
    token_kategoripenjualan = models.CharField(max_length=300, blank=True, null=True)
    tanggal_upload = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True)
    
    class Meta:
        verbose_name_plural = 'Data Kategori Penjualan'
    
    def __str__(self):
        return self.nama
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nama)
        # Auto-generate filter based on slug
        if not self.filter:
            self.filter = f"filter-{self.slug}"
        return super().save(*args, **kwargs)
    
class Produk(models.Model):
    kategoripenjualan = models.ForeignKey(KategoriPenjualan, null=True, blank=True, related_name="produks", on_delete=models.SET_NULL)
    nama = models.CharField(max_length=300, blank=True, null=True)
    deskripsi = RichTextField(blank=True, null=True)
    harga = models.CharField(max_length=300, blank=True, null=True)
    gambar = models.ImageField(upload_to='gambar', blank=False, null=True)
    aktif = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, blank=True, null=True, unique=True)
    tanggal_upload = models.DateTimeField(auto_now_add=True, null=True)
    token_produk = models.CharField(max_length=300, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Data Deskripsi'
        ordering = ['-tanggal_upload'] 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nama)
        super().save(*args, **kwargs)
    
    
    
    
# class ProdukDeskripsi(models.Model):
#     kategoripenjualan = models.ForeignKey(KategoriPenjualan, null=True, blank=True, related_name="produks", on_delete=models.SET_NULL)
#     nama = models.CharField(max_length=300, blank=True, null=True)
#     deskripsi = RichTextField(blank=True, null=True)
#     harga = models.CharField(max_length=300, blank=True, null=True)
#     gambar = models.ImageField(upload_to='gambar', blank=False, null=True)
#     aktif = models.BooleanField(default=True)
#     slug = models.SlugField(max_length=200, blank=True, null=True, unique=True)
#     tanggal_upload = models.DateTimeField(auto_now_add=True, null=True)
#     token_produk = models.CharField(max_length=300, blank=True, null=True)

    # class Meta:
    #     verbose_name_plural = 'Data Deskripsi'
    #     ordering = ['-tanggal_upload'] 

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.nama)
    #     super().save(*args, **kwargs)
    