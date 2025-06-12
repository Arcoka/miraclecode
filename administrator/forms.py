from django import forms
from django.utils import timezone
from datetime import timedelta
from .models import Kategori, Berita, Galeri, Layanan, Kontak, Pesan, Slide, Baground, VisiMisi, Pekerjaan, Team, ModelInkubasi, Testimoni, Profil, Pesan, Komentar, Faq, DaftarTenant, DaftarLayanan


class KategoriForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ['nama', 'aktif',]
        widgets = {
            'nama': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan nama kategori',
                'required': True, 
            }),
            'aktif': forms.CheckboxInput(attrs={
                'class': 'form-checkbox h-6 w-6 text-blue-600 focus:ring focus:ring-blue-200', 
            }),
        }
        labels = {
            'nama': 'Nama Kategori',
            'aktif': 'Status Aktif',
        }

#### BAGIAN BERITAA

class BeritaForm(forms.ModelForm):
    class Meta:
        model = Berita
        fields = ['kategori', 'judul', 'gambar', 'isi_berita', 'deskripsi']
        widgets = {
            'kategori': forms.Select(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'required': True, 
            }),
            'judul': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Judul Berita',
                'required': True, 
            }),
            'aktif': forms.CheckboxInput(attrs={
                'class': 'form-checkbox h-6 w-6 text-blue-600 focus:ring focus:ring-blue-200', 
            }),
            'gambar_berita': forms.ClearableFileInput(attrs={
                'class': 'file-input mt-1 block w-full text-gray-700 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-200 py-2',
                
            }),
            'isi_berita': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Isi Berita',
                'required': True, 
            }),
            'deskripsi': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Keterangan Berita',
                'required': True, 
            }),
        }

##### INI BAGIAN GALLERIIIII

class GaleriForm(forms.ModelForm):
    class Meta:
        model = Galeri
        fields = ['nama_galeri', 'gambar_galeri']
        widgets = {
            'nama_galeri': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Judul Galeri',
                'required': True, 
            }),
            'gambar_galeri': forms.ClearableFileInput(attrs={
                'class': 'file-input mt-1 block w-full text-gray-700 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-200 py-2',
                
            }),
            
        }


##### INI BAGIAN LAYANAN

class LayananForm(forms.ModelForm):
    class Meta:
        model = Layanan
        fields = ['nama', 'isi']
        widgets = {
            'nama': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Judul Layanan',
                'required': True, 
            }),
            'isi': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Isi Layanan',
                'required': True, 
            }),
            
        }


##### INI BAGIAN KONTAK
class KontakForm(forms.ModelForm):
    class Meta:
        model = Kontak
        fields = ['alamat', 'no_1', 'no_2', 'email','hari','jam']
        widgets = {
            'alamat': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Alamat',
                'required': True, 
            }),
            'no_1': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan No 1',
                'required': True, 
            }),
            'no_2': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan No 2',
                'required': True, 
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Email',
                'required': True, 
            }),
            'hari': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Hari Operasional',
                'required': True, 
            }),
            'jam': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Jam Operasional',
                'required': True, 
            }),
            
        }

##### INI BAGIAN SLIDE
class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = ['nama', 'teks_awal', 'teks_dua', 'gambar_slide']
        widgets = {
            'nama': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Judul Slide',
                'required': True, 
            }),
            'teks_awal': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Isi Slide',
                'required': True, 
            }),
            
            'gambar_slide': forms.ClearableFileInput(attrs={
                'class': 'file-input mt-1 block w-full text-gray-700 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-200 py-2',
                
            }),
            
        }

##### INI BAGIAN BAGROUND
class BagroundForm(forms.ModelForm):
    class Meta:
        model = Baground
        fields = ['nama_baground', 'gambar_baground']
        widgets = {
            'nama_baground': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Judul Baground',
                'required': True, 
            }),
            'gambar_baground': forms.ClearableFileInput(attrs={
                'class': 'file-input mt-1 block w-full text-gray-700 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-200 py-2',
                
            }),
            
        }


# Forms untuk field terpisah
class VisiForm(forms.ModelForm):
    class Meta:
        model = VisiMisi
        fields = ['visi']
        widgets = {
            'visi': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Visi',
                'required': True, 
            }),
        }

class MisiForm(forms.ModelForm):
    class Meta:
        model = VisiMisi
        fields = ['misi']
        widgets = {
            'misi': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Misi',
                'required': True, 
            }),
        }

class SasaranForm(forms.ModelForm):
    class Meta:
        model = VisiMisi
        fields = ['sasaran']
        widgets = {
            'sasaran': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Isi Sasaran',
                'required': True, 
            }),
        }

class TujuanForm(forms.ModelForm):
    class Meta:
        model = VisiMisi
        fields = ['tujuan']
        widgets = {
            'tujuan': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Isi Tujuan',
                'required': True, 
            }),
        }

# Tetap pertahankan form lengkap jika diperlukan
class VisiMisiForm(forms.ModelForm):
    class Meta:
        model = VisiMisi
        fields = ['visi','misi', 'sasaran','tujuan']
        widgets = {
            'visi': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Visi',
                'required': True, 
            }),
            'misi': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Misi',
                'required': True, 
            }),
            'sasaran': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Isi Sasaran',
                'required': True, 
            }),
            'tujuan': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Isi Tujuan',
                'required': True, 
            }),
        }

##### INI BAGIAN PEKERJAAN
class PekerjaanForm(forms.ModelForm):
    class Meta:
        model = Pekerjaan
        fields = ['judul', 'teks', 'gambar', 'nama', 'isi']
        widgets = {
            'judul': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Judul Kontak',
                'required': True, 
            }),
            'teks': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Isi Kontak',
                'required': True, 
            }),
            'gambar': forms.ClearableFileInput(attrs={
                'class': 'file-input mt-1 block w-full text-gray-700 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-200 py-2',
                
            }),
            'nama': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Isi Kontak',
                'required': True, 
            }),
            'isi': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Isi Kontak',
                'required': True, 
            }),
        }

##### INI BAGIAN TEAM
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['gambar', 'nama', 'jabatan','facebook', 'twitter', 'instagram']
        widgets = {
            'gambar': forms.ClearableFileInput(attrs={
                'class': 'file-input mt-1 block w-full text-gray-700 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-200 py-2',
                
            }),
            'nama': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Judul Kontak',
                'required': True, 
            }),
            'jabatan': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Isi Kontak',
                'required': True, 
            }),
            
            'facebook': forms.URLInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Link Facebook',
                'required': True, 
            }),
            'twitter': forms.URLInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan link Twitter',
                'required': True, 
            }),
            'instagram': forms.URLInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Link Instagram',
                'required': True, 
            }),
            
        }


##### INI BAGIAN MODELINKUBASI
class ModelInkubasiForm(forms.ModelForm):
    class Meta:
        model = ModelInkubasi
        fields = ['nama','gambar','deskripsi']
        widgets = {
            'gambar': forms.ClearableFileInput(attrs={
                'class': 'file-input mt-1 block w-full text-gray-700 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-200 py-2',
            }),
            'nama': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Judul Kontak',
                'required': True, 
            }),
            'deskripsi': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Isi Kontak',
                'required': True, 
            }),
        }

##### INI BAGIAN TESTIMONI
class TestimoniForm(forms.ModelForm):
    class Meta:
        model = Testimoni
        fields = ['deskripsi','gambar','nama', 'jabatan']
        widgets = {
            'deskripsi': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Isi Testimoni',
                'required': True, 
            }),
            'gambar': forms.ClearableFileInput(attrs={
                'class': 'file-input mt-1 block w-full text-gray-700 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-200 py-2',
            }),
            'nama': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Nama Pengirim',
                'required': True, 
            }),
            'jabatan': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Jabatan Pengirim',
                'required': True, 
            }),
        }

##### INI BAGIAN Profil
class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['judul','deskripsi', 'gambar', 'gambar_2']
        widgets = {
            'judul': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Judul Profil',
                'required': True, 
            }),
            'deskripsi': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Isi Profil',
                'required': True, 
            }),
            'gambar': forms.ClearableFileInput(attrs={
                'class': 'file-input mt-1 block w-full text-gray-700 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-200 py-2',
                
            }),
            'gambar_2': forms.ClearableFileInput(attrs={
                'class': 'file-input mt-1 block w-full text-gray-700 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-200 py-2',
                
            }),
            
        }

##### INI BAGIAN PESAN
class PesanForm(forms.ModelForm):
    class Meta:
        model = Pesan
        fields = ['nama', 'email', 'pesan']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Anda'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Anda'}),
            'pesan': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tulis pesan Anda di sini', 'rows': 5}),
        }

##### INI BAGIAN DAFTAR TENANT
class DaftarTenantForm(forms.ModelForm):
    class Meta:
        model = DaftarTenant
        fields = ['nama', 'email', 'telepon', 'namausaha', 'jenisusaha']
        # Tambahkan field lainnya jika ada
        
        # Tambahkan widget untuk styling form
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Nama Lengkap'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'contoh@email.com'}),
            'telepon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nomor Telepon/WhatsApp'}),
            'namausaha': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Usaha Anda'}),
            'jenisusaha': forms.Select(attrs={'class': 'form-select'}),
        }
        
    # Validasi untuk email
    def clean_email(self):
        # Pastikan self.cleaned_data sudah ada sebelum mencoba mengakses
        if hasattr(self, 'cleaned_data'):
            email = self.cleaned_data.get('email')
            if email:  # Pastikan email tidak None
                # Cek apakah email sudah ada di database
                if DaftarTenant.objects.filter(email=email).exists():
                    raise forms.ValidationError("Email ini sudah terdaftar dalam sistem.")
                return email
        return None  # Jika tidak ada data, kembalikan None
    

class DaftarLayananForm(forms.ModelForm):
    """Form untuk pengguna mengisi permintaan layanan"""
    
    class Meta:
        model = DaftarLayanan
        fields = ['nama', 'email', 'alamat', 'telepon', 'jenislayanan', 'jenisproduk', 'waktu', 'pesan']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nama lengkap'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan email'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Masukkan alamat lengkap', 'rows': 3}),
            'telepon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nomor telepon'}),
            'jenislayanan': forms.Select(attrs={'class': 'form-select'}),
            'jenisproduk': forms.Select(attrs={'class': 'form-select'}),
            'waktu': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'pesan': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Masukkan pesan atau keterangan tambahan', 'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set default waktu to current time + 1 day
        if not self.initial.get('waktu'):
            self.initial['waktu'] = timezone.now() + timezone.timedelta(days=1)
        
        # Add required attribute
        for field_name in ['nama', 'email', 'telepon', 'jenislayanan', 'jenisproduk', 'waktu']:
            self.fields[field_name].required = True
        
        # Add help text
        self.fields['waktu'].help_text = "Pilih tanggal dan waktu yang diinginkan untuk layanan"
        self.fields['telepon'].help_text = "Masukkan nomor telepon yang aktif"
        
##### INI BAGIAN PESAN
class KomentarForm(forms.ModelForm):
    class Meta:
        model = Komentar
        fields = ['nama', 'email', 'komentar']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Anda'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Anda'}),
            'komentar': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tulis komentar Anda di sini', 'rows': 5}),
        }

##### INI BAGIAN SLIDE
class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['noslug', 'tanya', 'jawab']
        widgets = {
            'noslug': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Kunci Slug',
                'required': True, 
            }),
            'tanya': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Isi Pertanyaan',
                'required': True, 
            }),
            
            'jawab': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200 py-2',  
                'placeholder': 'Masukkan Isi Jawaban',
                'required': True, 
            }),
            
        }
