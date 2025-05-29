from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from administrator.models import Slide, Berita, Kategori, Team, Testimoni, Profil, Kontak, Pesan, VisiMisi, Faq, DaftarTenant, Baground, Sejarah, DaftarLayanan, Layanan, JenisLayanan, ModelInkubasi, Seleksi, TenantInkubator
from cart.models import SlidePenjualan, Jasa, KategoriPenjualan, Produk
from django.utils.text import slugify
from administrator.forms import PesanForm, KomentarForm, DaftarTenantForm, DaftarLayananForm
import uuid
from django.contrib import messages
from django.urls import reverse
import logging
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.db import IntegrityError

logger = logging.getLogger(__name__)


# from .models import Berita  # Pastikan model diimport

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Jika user adalah admin, redirect ke halaman admin
            if user.is_staff:  # `is_staff` berarti admin Django
                return redirect("berandaadmin")  # Redirect ke dashboard admin
            
            # Jika bukan admin, bisa redirect ke halaman lain
            return redirect("home")  # Sesuaikan dengan URL beranda kamu

        else:
            return render(request, "login.html", {"error": "Username atau password salah!"})

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")  # Arahkan kembali ke halaman login setelah logout


# def beranda(request): 
#     query_slide = Slide.objects.filter(aktif=True).order_by('-id')
#     # query_profil = Profil.objects.filter(aktif=True).order_by('-id')
#     # query_study = Study.objects.filter(aktif=True).order_by('-id')
#     isi = {
#         "judul": "Halaman Beranda", 
#         "slide": query_slide
#         # "profil": query_profil,
#         # "study": query_study
#     } 
#     return render(request, 'beranda.html', isi)

def beranda(request):
    query_slide = Slide.objects.filter(aktif=True).order_by('-id')
    query_team = Team.objects.filter(aktif=True).order_by('-id')
    query_testimoni = Testimoni.objects.filter(aktif=True).order_by('-id')
    query_profil = Profil.objects.filter(aktif=True).order_by('-id')
    query_kontak = Kontak.objects.filter(aktif=True).order_by('-id')
    berita_terbaru = Berita.objects.order_by('-tanggal_upload')[:3]
    query_baground = Baground.objects.filter(aktif=True).order_by('-id')
    
    if request.method == 'POST':
        form = PesanForm(request.POST)
        if form.is_valid():
            pesan = form.save(commit=False) # Get unsaved object
            pesan.save()  # Save the object to the database
            messages.success(request, 'Pesan Anda telah berhasil dikirim!')
            return redirect('home')
    else:
        form = PesanForm()
    
    isi = {
        "judul": "Halaman Beranda",
        "slide": query_slide,
        "baground": query_baground,
        "team": query_team,
        "testimoni": query_testimoni,
        "profil": query_profil,
        "kontak": query_kontak,
        "berita": berita_terbaru,
        "form": form,  # Form sudah ditambahkan ke dalam context
    }
    return render(request, 'beranda.html', isi)

def berandapenjualan(request):
    query_slidepenjualan = SlidePenjualan.objects.filter(aktif=True).order_by('-id')
    query_jasa = Jasa.objects.filter(aktif=True).order_by('-id')
    query_kategoripenjualan = KategoriPenjualan.objects.filter(aktif=True).order_by('-id')
    query_produk = Produk.objects.filter(aktif=True).order_by('-id')
    # query_kontak = Kontak.objects.filter(aktif=True).order_by('-id')
    # berita_terbaru = Berita.objects.order_by('-tanggal_upload')[:3]
    
    # if request.method == 'POST':
    #     form = PesanForm(request.POST)
    #     if form.is_valid():
    #         pesan = form.save(commit=False) # Get unsaved object
    #         pesan.save()  # Save the object to the database
    #         messages.success(request, 'Pesan Anda telah berhasil dikirim!')
    #         return redirect('home')
    # else:
    #     form = PesanForm()
    
    isi = {
        "judul": "Halaman Beranda",
        "slidepenjualan": query_slidepenjualan,
        "jasa": query_jasa,
        "kategoripenjualan": query_kategoripenjualan,
        "produk": query_produk,
        # "kontak": query_kontak,
        # "berita": berita_terbaru,
        # "form": form,  # Form sudah ditambahkan ke dalam context
    }
    return render(request, 'penjualan.html', isi)

def berita_detail(request, slug): 
    berita = get_object_or_404(Berita, slug=slug)  # Ambil berita berdasarkan slug
    if request.method == 'POST':
        form = KomentarForm(request.POST)
        if form.is_valid():
            komentar = form.save(commit=False) # Get unsaved object
            komentar.save()  # Save the object to the database
            messages.success(request, 'Komentar Anda telah berhasil dikirim!')
            
    else:
        form = KomentarForm()

    context = {
        "judul": berita.judul, 
        "berita": berita,
        "form": form  # Form sudah ditambahkan ke dalam context
    }
    return render(request, 'berita.html', context)

def berita_list(request):
    berita_list = Berita.objects.all().order_by('-tanggal_upload')  # Ambil semua berita, diurutkan dari terbaru
    paginator = Paginator(berita_list, 12)  # 12 berita per halaman
    page_number = request.GET.get('page')  # Ambil nomor halaman dari query string
    berita_page = paginator.get_page(page_number)  # Ambil objek berita berdasarkan halaman
    query_kategori = Kategori.objects.filter(aktif=True).order_by('-id')
    context = { 
        "kategori": query_kategori
        
    }
    return render(request, 'beritalist.html', {'berita_list': berita_page})


def jasa(request): 
    query_jasa = Jasa.objects.filter(aktif=True).order_by('-id')
    # query_study = Study.objects.filter(aktif=True).order_by('-id')
    isi = {
        "judul": "Halaman Penjualan", 
        "jasa": query_jasa,
    } 
    return render(request, 'penjualan.html', isi)

def profil(request): 
    query_profil = Profil.objects.filter(aktif=True).order_by('-id')
    isi = {
        "judul": "Halaman Profil", 
        "profil": query_profil
    } 
    return render(request, 'beranda.html', isi)

def team(request): 
    query_team = Team.objects.filter(aktif=True).order_by('-id')
    isi = {
        "judul": "Halaman Team", 
        "team": query_team  # Ubah dari "profil" menjadi "team" agar sesuai dengan template
    } 
    return render(request, 'team.html', isi)  # Gunakan template khusus team

def profil(request): 
    query_slide = Slide.objects.filter(aktif=True).order_by('-id')
    query_profil = Profil.objects.filter(aktif=True).order_by('-id')
    isi = {
        "judul": "Halaman Profil", 
        "profil": query_profil,
        "slide": query_slide
    } 
    return render(request, 'profil.html', isi)  

def faq(request): 
    query_slide = Slide.objects.filter(aktif=True).order_by('-id')
    query_faq = Faq.objects.filter(aktif=True).order_by('-id')
    isi = {
        "judul": "Halaman Faq", 
        "faq": query_faq,
        "slide": query_slide
    } 
    return render(request, 'faq.html', isi)  

def jenislayanan(request): 
    query_slide = Slide.objects.filter(aktif=True).order_by('-id')
    query_jenislayanan = JenisLayanan.objects.filter(aktif=True).order_by('-id')
    isi = {
        "judul": "Halaman Faq", 
        "jenislayanan": query_jenislayanan,
        "slide": query_slide
    } 
    return render(request, 'jenislayanan.html', isi)  

def visimisi(request): 
    query_slide = Slide.objects.filter(aktif=True).order_by('-id')
    
    # Ambil data visi, misi, sasaran, dan tujuan secara terpisah
    visi_list = VisiMisi.objects.filter(visi__isnull=False, aktif=True).order_by('-id')
    misi_list = VisiMisi.objects.filter(misi__isnull=False, aktif=True).order_by('-id')
    sasaran_list = VisiMisi.objects.filter(sasaran__isnull=False, aktif=True).order_by('-id')
    tujuan_list = VisiMisi.objects.filter(tujuan__isnull=False, aktif=True).order_by('-id')
    
    isi = {
        "judul": "Halaman Profil", 
        "visi_list": visi_list,
        "misi_list": misi_list,
        "sasaran_list": sasaran_list,
        "tujuan_list": tujuan_list,
        "slide": query_slide
    } 
    return render(request, 'visimisi.html', isi)

def kontak(request):
    query_kontak = Kontak.objects.filter(aktif=True).order_by('-id')
    query_slide = Slide.objects.filter(aktif=True).order_by('-id')
    if request.method == 'POST':
        form = PesanForm(request.POST)
        if form.is_valid():
            pesan = form.save(commit=False) # Get unsaved object
            pesan.save()  # Save the object to the database
            messages.success(request, 'Pesan Anda telah berhasil dikirim!')
            return redirect('kontak')
    else:
        form = PesanForm()
    isi = {
        "judul": "Informasi Kontak",
        "kontak": query_kontak,
        "slide": query_slide,
        "form": form,
    }
    return render(request, 'kontak.html', isi)

def hubungi_kami(request):
    if request.method == "POST":
        form = PesanForm(request.POST)
        if form.is_valid():
            try:
                pesan = form.save(commit=False)
                pesan.token_pesan = str(uuid.uuid4())
                pesan.slug = slugify(pesan.nama) if pesan.nama else str(uuid.uuid4())
                pesan.save()
                messages.success(request, 'Pesan terkirim!')
                return redirect('hubungi_kami')
            except Exception as e:
                print("Error saving:", e)  # Debugging
                messages.error(request, 'Terjadi kesalahan sistem')
        else:
            print("Form errors:", form.errors)  # Debugging
            messages.error(request, 'Isi form dengan benar')
    else:
        form = PesanForm()
    
    return render(request, 'hubungikami.html', {'form': form})

def komentar_pelanggan(request):
    if request.method == "POST":
        form = KomentarForm(request.POST)
        if form.is_valid():
            try:
                komentar = form.save(commit=False)
                komentar.token_komentar = str(uuid.uuid4())
                komentar.slug = slugify(komentar.nama) if komentar.nama else str(uuid.uuid4())
                komentar.save()
                messages.success(request, 'Komentar terkirim!')
                return redirect('komentar_pelanggan')
            except Exception as e:
                print("Error saving:", e)  # Debugging
                messages.error(request, 'Terjadi kesalahan sistem')
        else:
            print("Form errors:", form.errors)  # Debugging
            messages.error(request, 'Isi form dengan benar')
    else:
        form = KomentarForm()
    
    return render(request, 'komentarpelanggan.html', {'form': form})

def daftar_tenant(request):
    # Mengambil slide yang aktif, diurutkan berdasarkan ID terbaru
    query_slide = Slide.objects.filter(aktif=True).order_by('-id')

    # Cek apakah request adalah POST untuk menghandle form
    if request.method == "POST":
        # Perbaikan 1: Tambahkan request.FILES untuk menangani upload file
        form = DaftarTenantForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Menyimpan data tenant yang telah diisi
                daftartenant = form.save(commit=False)
                
                # Membuat token unik menggunakan uuid
                daftartenant.token_daftartenant = str(uuid.uuid4())
                
                # Membuat slug menggunakan nama, atau uuid jika nama tidak ada
                nama_slug = daftartenant.nama if daftartenant.nama else str(uuid.uuid4())
                base_slug = slugify(nama_slug)
                
                # Pastikan slug unik dengan menambahkan random string jika diperlukan
                if DaftarTenant.objects.filter(slug=base_slug).exists():
                    daftartenant.slug = f"{base_slug}-{str(uuid.uuid4())[:8]}"
                else:
                    daftartenant.slug = base_slug
                
                # Perbaikan 2: Cek integritas data sebelum menyimpan
                daftartenant.clean()  # Ini akan memvalidasi model-level constraints
                
                # Simpan data tenant ke database
                daftartenant.save()
                
                # Perbaikan 3: Tambahkan log untuk berhasil
                logger.info(f"Tenant berhasil terdaftar: {daftartenant.nama} ({daftartenant.email})")
                
                # Menampilkan pesan sukses jika data berhasil disimpan
                messages.success(request, 'Pendaftaran tenant berhasil dikirim! Terima kasih.')
                
                # Perbaikan 4: Redirect dengan parameter untuk konfirmasi
                return redirect('daftar_tenant_sukses')
            except ValidationError as ve:
                # Perbaikan 5: Tangani error validasi model secara spesifik
                messages.error(request, f'Validasi gagal: {ve}')
                logger.warning(f"Validasi tenant gagal: {ve}")
            except IntegrityError as ie:
                # Perbaikan 6: Tangani error integritas database (seperti duplikat)
                messages.error(request, 'Data yang Anda masukkan mungkin sudah terdaftar.')
                logger.warning(f"Integrity error: {ie}")
            except Exception as e:
                # Menampilkan pesan error jika ada masalah saat menyimpan data
                messages.error(request, 'Terjadi kesalahan sistem. Coba lagi.')
                # Perbaikan 7: Log error lebih detail
                logger.error(f"Error saat menyimpan tenant: {e}", exc_info=True)
        else:
            # Menampilkan form error jika form tidak valid
            logger.warning(f"Form errors: {form.errors}")
            for field, errors in form.errors.items():
                for error in errors:
                    # Perbaikan 8: Tampilkan error per field untuk user
                    messages.error(request, f'Error pada {field}: {error}')
    else:
        form = DaftarTenantForm()  # Menampilkan form kosong jika request bukan POST

    # Menyusun konteks untuk mengirimkan data ke template
    context = {
        "slide": query_slide,  # Data slide untuk tampilan
        "form": form,  # Form untuk pendaftaran tenant
        "page_title": "Pendaftaran Tenant Inkubator Bisnis",  # Perbaikan 9: Tambahkan judul halaman
    }
    
    # Render halaman dengan data yang dikirimkan
    return render(request, 'daftartenantinkubator.html', context)

def toggle_aktif(request, id):
    # Ambil objek tenant berdasarkan ID, jika tidak ada akan tampil 404
    tenant = get_object_or_404(DaftarTenant, id=id)

    # Ubah nilai aktif (jika True jadi False, jika False jadi True)
    tenant.aktif = not tenant.aktif
    tenant.save()

    # Beri pesan sukses (opsional)
    if tenant.aktif:
        messages.success(request, f"Tenant '{tenant.nama}' telah diaktifkan.")
    else:
        messages.warning(request, f"Tenant '{tenant.nama}' telah dinonaktifkan.")

    # Redirect kembali ke halaman daftar tenant
    return redirect('daftartenant_list')  # Pastikan nama URL ini sesuai

# def daftar_tenant_sukses(request):
#     return render(request, 'daftar_tenant_sukses.html', {
#         'page_title': 'Pendaftaran Berhasil'
#     })


# def pesanadmin(request):
#     pesan = Pesan.objects.all()
#     context = {
#         'pesan': pesan
#     }
#     return render(request, 'pesanadmin.html', context)

def kategori(request): 
    query_kategori = Kategori.objects.filter(aktif=True).order_by('-id')
    isi = {
        "judul": "Halaman Kategori", 
        "kategori": query_kategori
    } 
    return render(request, 'berita.html', isi)

# View untuk menampilkan halaman produk yang bisa difilter
def produkdisplay(request):
    produk = Produk.objects.filter(aktif=True)
    kategoripenjualan = KategoriPenjualan.objects.filter(aktif=True)
    
    context = {
        'produk': produk,
        'kategoripenjualan': kategoripenjualan,
    }
    return render(request, 'produkdisplay.html', context)  # Mengubah template ke yang baru dibuat

def produk_detail(request, slug): 
    produk = get_object_or_404(Produk, slug=slug)  # Ambil produk berdasarkan slug
    # if request.method == 'POST':
    #     form = KomentarForm(request.POST)
    #     if form.is_valid():
    #         komentar = form.save(commit=False) # Get unsaved object
    #         komentar.save()  # Save the object to the database
    #         messages.success(request, 'Komentar Anda telah berhasil dikirim!')
            
    # else:
    #     form = KomentarForm()

    context = {
        "nama": produk.nama, 
        "produk": produk,
        # "form": form  # Form sudah ditambahkan ke dalam context
    }
    return render(request, 'produk_detail.html', context)

def produk_list(request):
    produk_list = Produk.objects.all().order_by('-tanggal_upload')  # Ambil semua produk, diurutkan dari terbaru
    paginator = Paginator(produk_list, 12)  # 12 produk per halaman
    page_number = request.GET.get('page')  # Ambil nomor halaman dari query string
    produk_page = paginator.get_page(page_number)  # Ambil objek produk berdasarkan halaman
    query_kategori = Kategori.objects.filter(aktif=True).order_by('-id')
    context = { 
        "kategori": query_kategori
        
    }
    return render(request, 'produk.html', {'produk_list': produk_page})


def baground(request): 
    query_baground = baground.objects.filter(aktif=True).order_by('-id')
    isi = {
        "judul": "Halaman Slide", 
        "baground": query_baground
    } 
    return render(request, 'beranda.html', isi)

def sejarah(request): 
    query_sejarah = Sejarah.objects.filter(aktif=True).order_by('-id')
    
    isi = {
        "judul": "Halaman Model Inkubasi", 
        "sejarah": query_sejarah,
       
    } 
    return render(request, 'sejarah.html', isi)

def layanan(request): 
    query_layanan = Layanan.objects.order_by('-id')
    isi = { 
        "layanan": query_layanan
    } 
    return render(request, 'layanan.html', isi)

def submit_layanan(request):
    """View untuk user mengisi form layanan"""
    if request.method == 'POST':
        form = DaftarLayananForm(request.POST)
        query_slide = Slide.objects.filter(aktif=True).order_by('-id')
        query_layanan = Layanan.objects.order_by('-id')
        if form.is_valid():
            layanan = form.save()
            messages.success(request, 'Permintaan layanan Anda berhasil dikirim! Kami akan menghubungi Anda segera.')
            # return redirect(reverse('konfirmasi_layanan', kwargs={'slug': layanan.slug}))
    else:
        form = DaftarLayananForm()
        query_slide = Slide.objects.filter(aktif=True).order_by('-id')
        query_layanan = Layanan.objects.order_by('-id')
    
    return render(request, 'form_layanan.html', {
        'form': form,
        "slide": query_slide,
        "layanan": query_layanan,
        'title': 'Form Permintaan Layanan'
    })

def konfirmasi_layanan(request, slug):
    """View konfirmasi setelah submit layanan"""
    try:
        layanan = get_object_or_404(DaftarLayanan, slug=slug)
        return render(request, 'konfirmasi_layanan', {
            'layanan': layanan,
            'title': 'Konfirmasi Permintaan Layanan'
        })
    except:
        raise Http404("Halaman tidak ditemukan")

def cek_status_layanan(request):
    """View untuk cek status layanan dengan token"""
    token = request.GET.get('token', None)
    layanan = None
    
    if token:
        layanan = DaftarLayanan.objects.filter(token_daftarlayanan=token, aktif=True).first()
    
    return render(request, 'cek_status.html', {
        'layanan': layanan,
        'token': token,
        'title': 'Cek Status Layanan'
    })


def modelinkubasi(request): 
    query_modelinkubasi = ModelInkubasi.objects.filter(aktif=True).order_by('-id')
    query_slide = Slide.objects.filter(aktif=True).order_by('-id')
    isi = {
        "judul": "Halaman Model Inkubasi", 
        "modelinkubasi": query_modelinkubasi,
        "slide": query_slide,
    } 
    return render(request, 'modelinkubasi.html', isi)

def tenantinkubator(request): 
    query_tenantinkubator = TenantInkubator.objects.filter(aktif=True).order_by('-id')
    
    isi = {
        "judul": "Halaman Model Inkubasi", 
        "tenantinkubator": query_tenantinkubator,
       
    } 
    return render(request, 'tenantinkubator.html', isi)



def testimoni(request): 
    query_testimoni = Testimoni.objects.filter(aktif=True).order_by('-id')
    isi = {
        "judul": "Halaman Testimoni", 
        "testimoni": query_testimoni  # Ubah dari "profil" menjadi "team" agar sesuai dengan template
    } 
    return render(request, 'beranda.html', isi)  # Gunakan template khusus team

def seleksi(request): 
    query_seleksi = Seleksi.objects.filter(aktif=True).order_by('-id')
    query_slide = Slide.objects.filter(aktif=True).order_by('-id')
    isi = {
        "judul": "Halaman Model Inkubasi", 
        "seleksi": query_seleksi,
        "slide": query_slide,
    } 
    return render(request, 'seleksi.html', isi)

# def Pagelogin(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user_obj = User.objects.filter(username = username).first()
#         if user_obj is None:
#             messages.success(request, 'Username Tidak ditemukan')
#             return redirect('login')
#         cocokan = authenticate(request, username=username, password=password)
#         if cocokan is None:
#             messages.success(request, 'Password salah')
#             return redirect('login')
#         if cocokan is not None:
#             login(request, cocokan)
#             return redirect('berandaadmin') 

#     context = {
#             "judul": "Halaman Login",  
#     }
#     return render(request, 'login.html', context)

# def logoutPage(request):
#     logout(request)
#     return redirect('login')
