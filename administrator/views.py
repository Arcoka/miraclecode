from django.shortcuts import render, get_object_or_404, redirect
from .models import Berita, Galeri, Slide, Kategori, Layanan, Kontak, Baground, VisiMisi, Pekerjaan, Team, ModelInkubasi, Testimoni, Profil, Pesan, Komentar, Faq, DaftarTenant, DaftarLayanan
from .forms import KategoriForm, BeritaForm, GaleriForm, LayananForm, KontakForm, SlideForm, BagroundForm,VisiMisiForm, PekerjaanForm, TeamForm, ModelInkubasiForm, TestimoniForm, ProfilForm, VisiForm, MisiForm, SasaranForm, TujuanForm, KomentarForm, FaqForm, DaftarTenantForm, DaftarLayananForm
import uuid
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils.timezone import now
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PesanForm
from .models import AdminPanelUser


# def active_users(request):
#     sessions = Session.objects.filter(expire_date__gte=now())
#     uid_list = []

#     for session in sessions:
#         data = session.get_decoded()
#         uid = data.get('_auth_user_id', None)
#         if uid:
#             uid_list.append(uid)

#     users = User.objects.filter(id__in=uid_list)
#     return render(request, 'admin/active_users.html', {'users': users})

# @login_required(login_url='login')

@login_required
def active_users(request):
    # Cek apakah user memiliki akses admin panel
    try:
        admin_profile = request.user.admin_panel_profile
    except:
        # Redirect ke halaman error atau home jika bukan admin panel user
        return render(request, 'error.html', {'message': 'Anda tidak memiliki akses ke halaman ini.'})
    
    # Jika bukan superadmin, tampilkan pesan error
    if not admin_profile.is_superadmin:
        return render(request, 'error.html', {'message': 'Hanya superadmin yang dapat mengakses halaman ini.'})
    
    # Dapatkan semua user yang memiliki AdminPanelUser profile
    admin_panel_users = AdminPanelUser.objects.all()
    users_with_profiles = [profile.user for profile in admin_panel_users]
    
    context = {
        'users': users_with_profiles,
        'admin_profiles': admin_panel_users,
    }
    
    return render(request, 'user_list.html', context)

@login_required
def add_admin_user(request):
    # Implementasi untuk menambah user baru
    # Hanya superadmin yang bisa menambah user
    if request.method == 'POST':
        # Logika untuk create user
        pass
    
    return render(request, 'add_user.html', {})

@login_required
def edit_admin_user(request, user_id):
    # Implementasi untuk edit user
    # Hanya superadmin yang bisa edit user
    user = User.objects.get(id=user_id)
    
    if request.method == 'POST':
        # Logika untuk update user
        pass
    
    return render(request, 'edit_user.html', {'user': user})

@login_required
def delete_admin_user(request, user_id):
    # Implementasi untuk delete user
    # Hanya superadmin yang bisa delete user
    user = User.objects.get(id=user_id)
    
    if request.method == 'POST':
        # Logika untuk delete user
        user.delete()
        return redirect('active_users')
    
    return render(request, 'delete_user.html', {'user': user})




def berandaadmin(request): 
    berita = Berita.objects.count()
    slide = Slide.objects.filter(aktif=True).count()
    galeri = Galeri.objects.filter(aktif=True).count()
    kategori = Kategori.objects.filter(aktif=True).count()
    layanan = Layanan.objects.count()
    isi = {
        "judul": "Halaman Administrator",
        'berita':berita,
        'slide':slide,
        'galeri':galeri,
        'menu':berandaadmin,
        'layanan':layanan,  
        
    } 
    return render(request, 'berandaadmin.html', isi)



####### INI BAGIAN KATEGORI
@login_required(login_url='login')
def kategoriadmin(request):
    kategori = Kategori.objects.order_by('-id')
    context = {
            "judul": "Data Kategori",
            "menu":"kategori",
            "kategori_list" : kategori
        }
    return render(request, 'kategoriadmin.html', context)

@login_required(login_url='login')
def formkategoriadmin(request):
    if request.method == "POST":
        token_kategori = str(uuid.uuid4())
        datadeskripsi = request.POST.get('deskripsi')
        form = KategoriForm(request.POST, request.FILES)  # Ambil data dari request
        if form.is_valid():  # Validasi form
            kategori = form.save(commit=False)  
            kategori.token_kategori = token_kategori
            kategori.deskripsi = datadeskripsi
            kategori.save()
            return redirect('kategoriadmin')  # Redirect ke halaman kategori setelah menyimpan
    else:
        form = KategoriForm()  # Tampilkan form kosong jika GET request
    context = {
        "judul": "Form Kategori",
        "menu": "kategori",
        "form": form
    }
    return render(request, 'formkategoriadmin.html', context)

@login_required(login_url='login')
def editkategoriadmin(request, token):
    kategori = get_object_or_404(Kategori, token_kategori=token) #memanggil satu data yang kategorinya sama maka satu yang lainnya tidak akan tertampil
    if request.method == "POST":
        datadeskripsi = request.POST.get('deskripsi')
        form = KategoriForm(request.POST, request.FILES, instance=kategori)
        if form.is_valid():
            kategoriedit = form.save(commit=False)
            kategoriedit.deskripsi = datadeskripsi
            kategoriedit.save()
            return redirect('kategoriadmin')  # Redirect ke halaman daftar kategori
    else:
        form = KategoriForm(instance=kategori)
    context = {
        "judul": "Form Edit Kategori",
        "menu": "kategori",
        "form": form,
        'kategori': kategori
    }
    return render(request, 'formkategoriadmin.html', context)

@login_required(login_url='login')
def deletekategoriadmin(request, token):
    kategori = get_object_or_404(Kategori, token_kategori=token)
    if request.method == 'POST':
        kategori.delete()
        return redirect('kategoriadmin')  
    return redirect('kategoriadmin')

########  INI BAGIAN BERITA

@login_required(login_url='login')
def beritaadmin(request):
    berita = Berita.objects.order_by('-id')
    context = {
            "judul": "Data Berita",
            "menu":"berita",
            "berita_list" : berita
        }
    return render(request, 'beritaadmin.html', context)

@login_required(login_url='login')
def formberitaadmin(request):
    if request.method == "POST":
        token_berita = str(uuid.uuid4())
        datadeskripsi = request.POST.get('deskripsi')
        
        form = BeritaForm(request.POST, request.FILES)  # Ambil data dari request
        if form.is_valid():  # Validasi form
            berita = form.save(commit=False)  
            berita.token_berita = token_berita
            berita.deskripsi = datadeskripsi
            berita.save()
            return redirect('beritaadmin')  # Redirect ke halaman berita setelah menyimpan
    else:
        form = BeritaForm()  # Tampilkan form kosong jika GET request
    context = {
        "judul": "Form Berita",
        "menu": "berita",
        "form": form
    }
    return render(request, 'formberitaadmin.html', context)

@login_required(login_url='login')
def editberitaadmin(request, token):
    berita = get_object_or_404(Berita, token_berita=token) #memanggil satu data yang beritanya sama maka satu yang lainnya tidak akan tertampil
    if request.method == "POST":
        #datadeskripsi = request.POST.get('deskripsi')
        form = BeritaForm(request.POST, request.FILES, instance=berita)
        if form.is_valid():
            form.save()
            #beritaedit.deskripsi = datadeskripsi
            #beritaedit.save()
            return redirect('beritaadmin')  # Redirect ke halaman daftar berita
    else:
        form = BeritaForm(instance=berita)
    context = {
        "judul": "Form Edit Berita",
        "menu": "berita",
        "form": form,
        'berita': berita
    }
    return render(request, 'formberitaadmin.html', context)

@login_required(login_url='login')
def deleteberitaadmin(request, token):
    berita = get_object_or_404(Berita, token_berita=token)
    if request.method == 'POST':
        berita.delete()
        return redirect('beritaadmin')  
    return redirect('beritaadmin')


##### INI BAGIAN GALERIIIIII
@login_required(login_url='login')
def galeriadmin(request):
    galeri = Galeri.objects.order_by('-id')
    context = {
            "judul": "Data Galeri",
            "menu":"galeri",
            "galeri_list" : galeri
        }
    return render(request, 'galeriadmin.html', context)

@login_required(login_url='login')
def formgaleriadmin(request):
    if request.method == "POST":
        token_galeri = str(uuid.uuid4())
        #datadeskripsi = request.POST.get('deskripsi')
        form = GaleriForm(request.POST, request.FILES)  # Ambil data dari request
        if form.is_valid():  # Validasi form
            galeri = form.save(commit=False)  
            galeri.token_galeri = token_galeri
            #galeri.deskripsi = datadeskripsi
            galeri.save()
            return redirect('galeriadmin')  # Redirect ke halaman galeri setelah menyimpan
    else:
        form = GaleriForm()  # Tampilkan form kosong jika GET request
    context = {
        "judul": "Form Galeri",
        "menu": "galeri",
        "form": form
    }
    return render(request, 'formgaleriadmin.html', context)

@login_required(login_url='login')
def editgaleriadmin(request, token):
    galeri = get_object_or_404(Galeri, token_galeri=token) #memanggil satu data yang galerinya sama maka satu yang lainnya tidak akan tertampil
    if request.method == "POST":
        #datadeskripsi = request.POST.get('deskripsi')
        form = GaleriForm(request.POST, request.FILES, instance=galeri)
        if form.is_valid():
            form.save()
            #galeriedit.deskripsi = datadeskripsi
            #galeriedit.save()
            return redirect('galeriadmin')  # Redirect ke halaman daftar galeri
    else:
        form = GaleriForm(instance=galeri)
    context = {
        "judul": "Form Edit Galeri",
        "menu": "galeri",
        "form": form,
        'galeri': galeri
    }
    return render(request, 'formgaleriadmin.html', context)

@login_required(login_url='login')
def deletegaleriadmin(request, token):
    galeri = get_object_or_404(Galeri, token_galeri=token)
    if request.method == 'POST':
        galeri.delete()
        return redirect('galeriadmin')  
    return redirect('galeriadmin')

##### INI BAGIAN LAYANAN
@login_required(login_url='login')
def layananadmin(request):
    layanan = Layanan.objects.order_by('-id')
    context = {
            "judul": "Data Layanan",
            "menu":"layanan",
            "layanan_list" : layanan
        }
    return render(request, 'layananadmin.html', context)

@login_required(login_url='login')
def formlayananadmin(request):
    if request.method == "POST":
        token_layanan = str(uuid.uuid4())
        #datadeskripsi = request.POST.get('deskripsi')
        form = LayananForm(request.POST, request.FILES)  # Ambil data dari request
        if form.is_valid():  # Validasi form
            layanan = form.save(commit=False)  
            layanan.token_layanan = token_layanan
            #layanan.deskripsi = datadeskripsi
            layanan.save()
            return redirect('layananadmin')  # Redirect ke halaman layanan setelah menyimpan
    else:
        form = LayananForm()  # Tampilkan form kosong jika GET request
    context = {
        "judul": "Form Layanan",
        "menu": "layanan",
        "form": form
    }
    return render(request, 'formlayananadmin.html', context)


@login_required(login_url='login')
def editlayananadmin(request, token):
    layanan = get_object_or_404(Layanan, token_layanan=token) #memanggil satu data yang layanannya sama maka satu yang lainnya tidak akan tertampil
    if request.method == "POST":
        #datadeskripsi = request.POST.get('deskripsi')
        form = LayananForm(request.POST, request.FILES, instance=layanan)
        if form.is_valid():
            form.save()
            #layananedit.deskripsi = datadeskripsi
            #layananedit.save()
            return redirect('layananadmin')  # Redirect ke halaman daftar layanan
    else:
        form = LayananForm(instance=layanan)
    context = {
        "judul": "Form Edit Layanan",
        "form": form,
        'layanan': layanan
    }
    return render(request, 'formlayananadmin.html', context)

@login_required(login_url='login')
def deletelayananadmin(request, token):
    layanan = get_object_or_404(Layanan, token_layanan=token)
    if request.method == 'POST':
        layanan.delete()
        return redirect('layananadmin')  
    return redirect('layananadmin')


# BAGIAN KONTAK
@login_required(login_url='login')
def kontakadmin(request):
    kontak = Kontak.objects.order_by('-id')
    context = {
            "judul": "Data Kontak",
            "menu":"kontak",
            "kontak_list" : kontak
        }
    return render(request, 'kontakadmin.html', context)

@login_required(login_url='login')
def formkontakadmin(request):
    if request.method == "POST":
        token_kontak = str(uuid.uuid4())
        form = KontakForm(request.POST, request.FILES)
        if form.is_valid():
            kontak = form.save(commit=False)  
            kontak.token_kontak = token_kontak
            kontak.save()
            return redirect('kontakadmin')
    else:
        form = KontakForm()
    context = {
        "judul": "Form Kontak",
        "menu": "kontak",
        "form": form
    }
    return render(request, 'formkontakadmin.html', context)

@login_required(login_url='login')
def editkontakadmin(request, token):
    kontak = get_object_or_404(Kontak, token_kontak=token)
    if request.method == "POST":
        form = KontakForm(request.POST, request.FILES, instance=kontak)
        if form.is_valid():
            form.save()
            return redirect('kontakadmin')
    else:
        form = KontakForm(instance=kontak)
    context = {
        "judul": "Form Edit Kontak",
        "menu": "kontak",
        "form": form,
        'kontak': kontak
    }
    return render(request, 'formkontakadmin.html', context)

@login_required(login_url='login')
def deletekontakadmin(request, token):
    kontak = get_object_or_404(Kontak, token_kontak=token)
    if request.method == 'POST':
        kontak.delete()
        return redirect('kontakadmin')  
    return redirect('kontakadmin')



# BAGIAN PESAN KONTAK
@login_required
def pesan_list(request):
    pesan_list = Pesan.objects.filter(aktif=True).order_by('-tanggal_upload')
    belum_dibaca = pesan_list.filter(is_read=False).count()
    context = {
        'pesan_list': pesan_list,
        'belum_dibaca': belum_dibaca,
        'menu': 'pesan',  # Menandai menu "Pesan" aktif
    }
    return render(request, 'pesan_list.html', context)

@login_required
def pesan_detail(request, slug):
    pesan = get_object_or_404(Pesan, slug=slug)
    
    # Menandai pesan sebagai telah dibaca saat dibuka
    if not pesan.is_read:
        pesan.is_read = True
        pesan.save()
        
    return render(request, 'pesan_detail.html', {'pesan': pesan})

@login_required
def pesan_delete(request, slug):
    pesan = get_object_or_404(Pesan, slug=slug)
    
    if request.method == 'POST':
        # Soft delete - mengubah status aktif menjadi False
        pesan.aktif = False
        pesan.save()
        messages.success(request, 'Pesan berhasil dihapus')
        return redirect('pesan_list')
    
    # Jika bukan POST, tampilkan halaman konfirmasi
    return render(request, 'pesan_confirm_delete.html', {'pesan': pesan})

# Fungsi baru untuk toggle status tampil di website
@login_required
def toggle_tampil_di_website(request, slug):
    pesan = get_object_or_404(Pesan, slug=slug)
    
    if request.method == 'POST':
        # Toggle status tampil_di_website
        pesan.tampil_di_website = not pesan.tampil_di_website
        pesan.save()
        
        status = "ditampilkan di website" if pesan.tampil_di_website else "disembunyikan dari website"
        messages.success(request, f'Pesan berhasil {status}')
        
        # Kembali ke halaman yang sama (detail atau list)
        redirect_url = request.POST.get('next', 'pesan_list')
        return redirect(redirect_url)
    
    # Redirect ke halaman list jika bukan POST
    return redirect('pesan_list')




# BAGIAN PESAN KOMENTAR
def komentar_list(request):
    komentar_list = Komentar.objects.filter(aktif=True).order_by('-tanggal_upload')
    belum_dilihat = komentar_list.filter(is_read=False).count()
    context = {
        'komentar_list': komentar_list,
        'belum_dilihat': belum_dilihat,
        'menu': 'komentar',  # Menandai menu "Komentar" aktif
    }
    return render(request, 'komentar_list.html', context)

@login_required
def komentar_detail(request, slug):
    komentar = get_object_or_404(Komentar, slug=slug)
    
    # Menandai komentar sebagai telah dibaca saat dibuka
    if not komentar.is_read:
        komentar.is_read = True
        komentar.save()
        
    return render(request, 'komentar_detail.html', {'komentar': komentar})

@login_required
def komentar_delete(request, slug):
    komentar = get_object_or_404(Komentar, slug=slug)
    
    if request.method == 'POST':
        # Soft delete - mengubah status aktif menjadi False
        komentar.aktif = False
        komentar.save()
        messages.success(request, 'Komentar berhasil dihapus')
        return redirect('komentar_list')
    
    # Jika bukan POST, tampilkan halaman konfirmasi
    return render(request, 'komentar_confirm_delete.html', {'komentar': komentar})

@login_required
def toggle_tampil_di_website(request, slug):
    komentar = get_object_or_404(Komentar, slug=slug)
    
    if request.method == 'POST':
        # Toggle status tampil_di_website
        komentar.tampil_di_website = not komentar.tampil_di_website
        komentar.save()
        
        status = "ditampilkan di website" if komentar.tampil_di_website else "disembunyikan dari website"
        messages.success(request, f'Komentar berhasil {status}')
        
        # Kembali ke halaman yang sama (detail atau list)
        redirect_url = request.POST.get('next', 'komentar_list')
        return redirect(redirect_url)
    
    # Redirect ke halaman list jika bukan POST
    return redirect('komentar_list')


# BAGIAN DAFTAR TENANT
@login_required
def daftartenant_list(request):
    daftartenant_list = DaftarTenant.objects.filter(aktif=True).order_by('-tanggal_upload')
    belum_dibaca = daftartenant_list.filter(is_read=False).count()
    context = {
        'daftartenant_list': daftartenant_list,
        'belum_dibaca': belum_dibaca,
        'menu': 'daftartenant',  # Menandai menu "DaftarTenant" aktif
    }
    return render(request, 'daftartenant_list.html', context)

@login_required
def daftartenant_detail(request, slug):
    daftartenant = get_object_or_404(DaftarTenant, slug=slug)
    
    # Menandai daftartenant sebagai telah dibaca saat dibuka
    if not daftartenant.is_read:
        daftartenant.is_read = True
        daftartenant.save()
        
    return render(request, 'daftartenant_detail.html', {'daftartenant': daftartenant})

@login_required
def daftartenant_delete(request, slug):
    daftartenant = get_object_or_404(DaftarTenant, slug=slug)
    
    if request.method == 'POST':
        # Soft delete - mengubah status aktif menjadi False
        daftartenant.aktif = False
        daftartenant.save()
        messages.success(request, 'DaftarTenant berhasil dihapus')
        return redirect('daftartenant_list')
    
    # Jika bukan POST, tampilkan halaman konfirmasi
    return render(request, 'daftartenant_confirm_delete.html', {'daftartenant': daftartenant})


###untuk layanan

@login_required
def admin_daftar_layanan(request):
    """View admin untuk melihat semua layanan"""
    layanan_list = DaftarLayanan.objects.all().order_by('-tanggal_upload')
    return render(request, 'daftar_layanan.html', {
        'layanan_list': layanan_list,
        'title': 'Daftar Permintaan Layanan'
    })

@login_required
def admin_detail_layanan(request, slug):
    """View admin untuk melihat detail layanan"""
    layanan = get_object_or_404(DaftarLayanan, slug=slug)
    
    # Mark as read when viewed
    if not layanan.is_read:
        layanan.is_read = True
        layanan.save()
    
    return render(request, 'detail_layanan.html', {
        'layanan': layanan,
        'title': f'Detail Layanan - {layanan.nama}'
    })

@login_required
def admin_update_status(request, slug):
    """View admin untuk mengubah status aktif/nonaktif layanan"""
    layanan = get_object_or_404(DaftarLayanan, slug=slug)
    
    if request.method == "POST":
        status = request.POST.get('status', None)
        if status is not None:
            layanan.aktif = status == 'aktif'
            layanan.save()
            messages.success(request, f'Status layanan dari {layanan.nama} berhasil diperbarui')
        
    return redirect(reverse('admin_detail_layanan', kwargs={'slug': layanan.slug}))




##### INI BAGIAN SLIDE
@login_required(login_url='login')
def slideadmin(request):
    slide = Slide.objects.order_by('-id')
    context = {
            "judul": "Data Slide",
            "menu":"slide",
            "slide_list" : slide
        }
    return render(request, 'slideadmin.html', context)

@login_required(login_url='login')
def formslideadmin(request):
    if request.method == "POST":
        token_slide = str(uuid.uuid4())
        #datadeskripsi = request.POST.get('deskripsi')
        form = SlideForm(request.POST, request.FILES)  # Ambil data dari request
        if form.is_valid():  # Validasi form
            slide = form.save(commit=False)  
            slide.token_slide = token_slide
            #slide.deskripsi = datadeskripsi
            slide.save()
            return redirect('slideadmin')  # Redirect ke halaman slide setelah menyimpan
    else:
        form = SlideForm()  # Tampilkan form kosong jika GET request
    context = {
        "judul": "Form Slide",
        "menu": "slide",
        "form": form
    }
    return render(request, 'formslideadmin.html', context)

@login_required(login_url='login')
def editslideadmin(request, token):
    slide = get_object_or_404(Slide, token_slide=token) #memanggil satu data yang slidenya sama maka satu yang lainnya tidak akan tertampil
    if request.method == "POST":
        form = SlideForm(request.POST, request.FILES, instance=slide)
        if form.is_valid():
            form.save()
            #slideedit.deskripsi = datadeskripsi
            #slideedit.save()
            return redirect('slideadmin')  # Redirect ke halaman daftar slide
    else:
        form = SlideForm(instance=slide)
    context = {
        "judul": "Form Edit Slide",
        "menu": "slide",
        "form": form,
        'slide': slide
    }
    return render(request, 'formslideadmin.html', context)

@login_required(login_url='login')
def deleteslideadmin(request, token):
    slide = get_object_or_404(Slide, token_slide=token)
    if request.method == 'POST':
        slide.delete()
        return redirect('slideadmin')  
    return redirect('slideadmin')


##### INI BAGIAN BAGROUND
@login_required(login_url='login')
def bagroundadmin(request):
    baground = Baground.objects.order_by('-id')
    context = {
            "judul": "Data Baground",
            "menu":"baground",
            "baground_list" : baground
        }
    return render(request, 'bagroundadmin.html', context)

@login_required(login_url='login')
def formbagroundadmin(request):
    if request.method == "POST":
        token_baground = str(uuid.uuid4())
        #datadeskripsi = request.POST.get('deskripsi')
        form = BagroundForm(request.POST, request.FILES)  # Ambil data dari request
        if form.is_valid():  # Validasi form
            baground = form.save(commit=False)  
            baground.token_baground = token_baground
            #baground.deskripsi = datadeskripsi
            baground.save()
            return redirect('bagroundadmin')  # Redirect ke halaman baground setelah menyimpan
    else:
        form = BagroundForm()  # Tampilkan form kosong jika GET request
    context = {
        "judul": "Form Baground",
        "menu": "baground",
        "form": form
    }
    return render(request, 'formbagroundadmin.html', context)

@login_required(login_url='login')
def editbagroundadmin(request, token):
    baground = get_object_or_404(Baground, token_baground=token) #memanggil satu data yang bagroundnya sama maka satu yang lainnya tidak akan tertampil
    if request.method == "POST":
        form = BagroundForm(request.POST, request.FILES, instance=baground)
        if form.is_valid():
            form.save()
            #bagroundedit.deskripsi = datadeskripsi
            #bagroundedit.save()
            return redirect('bagroundadmin')  # Redirect ke halaman daftar baground
    else:
        form = BagroundForm(instance=baground)
    context = {
        "judul": "Form Edit Baground",
        "menu": "baground",
        "form": form,
        'baground': baground
    }
    return render(request, 'formbagroundadmin.html', context)

@login_required(login_url='login')
def deletebagroundadmin(request, token):
    baground = get_object_or_404(Baground, token_baground=token)
    if request.method == 'POST':
        baground.delete()
        return redirect('bagroundadmin')  
    return redirect('bagroundadmin')

@login_required(login_url='login')
def visimisiadmin(request):
    visimisi = VisiMisi.objects.order_by('-id')
    context = {
        "judul": "Data VisiMisi",
        "menu":"visimisi",
        "visimisi_list": visimisi
    }
    return render(request, 'visimisiadmin.html', context)

@login_required(login_url='login')
def formvisimisiadmin(request):
    jenis = request.GET.get('jenis', 'lengkap')
    form_class = None
    template = 'formvisimisiadmin.html'
    judul = "Form VisiMisi"
    
    # Pilih form berdasarkan jenis yang diminta
    if jenis == 'visi':
        form_class = VisiForm
        judul = "Tambah Visi"
        template = 'form_visi_admin.html'
    elif jenis == 'misi':
        form_class = MisiForm
        judul = "Tambah Misi"
        template = 'form_misi_admin.html'
    elif jenis == 'sasaran':
        form_class = SasaranForm
        judul = "Tambah Sasaran"
        template = 'form_sasaran_admin.html'
    elif jenis == 'tujuan':
        form_class = TujuanForm
        judul = "Tambah Tujuan"
        template = 'form_tujuan_admin.html'
    else:
        form_class = VisiMisiForm

    if request.method == "POST":
        token_visimisi = str(uuid.uuid4())
        form = form_class(request.POST, request.FILES)
        
        if form.is_valid():
            visimisi = form.save(commit=False)
            visimisi.token_visimisi = token_visimisi
            
            # Buat instance baru dengan hanya satu nilai
            if jenis != 'lengkap':
                # Set field lain ke None/kosong jika menggunakan form terpisah
                if jenis != 'visi': visimisi.visi = None
                if jenis != 'misi': visimisi.misi = None
                if jenis != 'sasaran': visimisi.sasaran = None
                if jenis != 'tujuan': visimisi.tujuan = None
                
            visimisi.save()
            return redirect('visimisiadmin')
    else:
        form = form_class()
    
    context = {
        "judul": judul,
        "menu": "visimisi",
        "form": form,
        "jenis": jenis
    }
    
    # Gunakan template sesuai jenis
    if jenis in ['visi', 'misi', 'sasaran', 'tujuan']:
        return render(request, f'form_{jenis}_admin.html', context)
    return render(request, 'formvisimisiadmin.html', context)

@login_required(login_url='login')
def editvisimisiadmin(request, token):
    visimisi = get_object_or_404(VisiMisi, token_visimisi=token)
    jenis = request.GET.get('jenis', 'lengkap')
    form_class = None
    
    # Tentukan jenis form berdasarkan data yang diedit
    if jenis == 'visi' or (visimisi.visi and not visimisi.misi and not visimisi.sasaran and not visimisi.tujuan):
        form_class = VisiForm
        judul = "Edit Visi"
    elif jenis == 'misi' or (not visimisi.visi and visimisi.misi and not visimisi.sasaran and not visimisi.tujuan):
        form_class = MisiForm
        judul = "Edit Misi"
    elif jenis == 'sasaran' or (not visimisi.visi and not visimisi.misi and visimisi.sasaran and not visimisi.tujuan):
        form_class = SasaranForm
        judul = "Edit Sasaran"
    elif jenis == 'tujuan' or (not visimisi.visi and not visimisi.misi and not visimisi.sasaran and visimisi.tujuan):
        form_class = TujuanForm
        judul = "Edit Tujuan"
    else:
        form_class = VisiMisiForm
        judul = "Edit VisiMisi"
    
    if request.method == "POST":
        form = form_class(request.POST, request.FILES, instance=visimisi)
        if form.is_valid():
            form.save()
            return redirect('visimisiadmin')
    else:
        form = form_class(instance=visimisi)
    
    context = {
        "judul": judul,
        "menu": "visimisi",
        "form": form,
        'visimisi': visimisi,
        "jenis": jenis
    }
    
    # Gunakan template sesuai jenis
    if jenis in ['visi', 'misi', 'sasaran', 'tujuan']:
        return render(request, f'form_{jenis}_admin.html', context)
    return render(request, 'formvisimisiadmin.html', context)

@login_required(login_url='login')
def deletevisimisiadmin(request, token):
    visimisi = get_object_or_404(VisiMisi, token_visimisi=token)
    
    if request.method == "POST":
        # Cek jenis hapus berdasarkan parameter jenis
        jenis = request.POST.get('jenis', 'lengkap')
        
        if jenis == 'lengkap':
            # Hapus seluruh record
            visimisi.delete()
        else:
            # Hapus/kosongkan field tertentu saja
            if jenis == 'visi':
                visimisi.visi = None
            elif jenis == 'misi':
                visimisi.misi = None
            elif jenis == 'sasaran':
                visimisi.sasaran = None
            elif jenis == 'tujuan':
                visimisi.tujuan = None
            
            # Simpan perubahan
            visimisi.save()
            
        return redirect('visimisiadmin')
    
    # Tentukan jenis hapus berdasarkan data yang ada
    jenis = 'lengkap'
    judul = "Hapus VisiMisi"
    
    if visimisi.visi and not visimisi.misi and not visimisi.sasaran and not visimisi.tujuan:
        jenis = 'visi'
        judul = "Hapus Visi"
    elif not visimisi.visi and visimisi.misi and not visimisi.sasaran and not visimisi.tujuan:
        jenis = 'misi'
        judul = "Hapus Misi"
    elif not visimisi.visi and not visimisi.misi and visimisi.sasaran and not visimisi.tujuan:
        jenis = 'sasaran'
        judul = "Hapus Sasaran"
    elif not visimisi.visi and not visimisi.misi and not visimisi.sasaran and visimisi.tujuan:
        jenis = 'tujuan'
        judul = "Hapus Tujuan"
    
    context = {
        "judul": judul,
        "menu": "visimisi",
        "visimisi": visimisi,
        "jenis": jenis
    }
    
    # Bisa juga membuat template konfirmasi hapus sesuai jenis
    if jenis in ['visi', 'misi', 'sasaran', 'tujuan']:
        return render(request, f'confirm_delete_{jenis}_admin.html', context)
    return render(request, 'confirm_delete_visimisi_admin.html', context)
##### INI BAGIAN PEKERJAAN
@login_required(login_url='login')
def pekerjaanadmin(request):
    pekerjaan = Pekerjaan.objects.order_by('-id')
    context = {
            "judul": "Data Pekerjaan",
            "menu":"pekerjaan",
            "pekerjaan_list" : pekerjaan
        }
    return render(request, 'pekerjaanadmin.html', context)

@login_required(login_url='login')
def formpekerjaanadmin(request):
    if request.method == "POST":
        token_pekerjaan = str(uuid.uuid4())
        #datadeskripsi = request.POST.get('deskripsi')
        form = PekerjaanForm(request.POST, request.FILES)  # Ambil data dari request
        if form.is_valid():  # Validasi form
            pekerjaan = form.save(commit=False)  
            pekerjaan.token_pekerjaan = token_pekerjaan
            #pekerjaan.deskripsi = datadeskripsi
            pekerjaan.save()
            return redirect('pekerjaanadmin')  # Redirect ke halaman pekerjaan setelah menyimpan
    else:
        form = PekerjaanForm()  # Tampilkan form kosong jika GET request
    context = {
        "judul": "Form Pekerjaan",
        "menu": "pekerjaan",
        "form": form
    }
    return render(request, 'formpekerjaanadmin.html', context)

@login_required(login_url='login')
def editpekerjaanadmin(request, token):
    pekerjaan = get_object_or_404(Pekerjaan, token_pekerjaan=token) #memanggil satu data yang pekerjaannya sama maka satu yang lainnya tidak akan tertampil
    if request.method == "POST":
        form = PekerjaanForm(request.POST, request.FILES, instance=pekerjaan)
        if form.is_valid():
            form.save()
            #pekerjaanedit.deskripsi = datadeskripsi
            #pekerjaanedit.save()
            return redirect('pekerjaanadmin')  # Redirect ke halaman daftar pekerjaan
    else:
        form = PekerjaanForm(instance=pekerjaan)
    context = {
        "judul": "Form Edit Pekerjaan",
        "menu": "pekerjaan",
        "form": form,
        'pekerjaan': pekerjaan
    }
    return render(request, 'formpekerjaanadmin.html', context)

@login_required(login_url='login')
def deletepekerjaanadmin(request, token):
    pekerjaan = get_object_or_404(Pekerjaan, token_pekerjaan=token)
    if request.method == 'POST':
        pekerjaan.delete()
        return redirect('pekerjaanadmin')  
    return redirect('pekerjaanadmin')

##### INI BAGIAN TEAM
@login_required(login_url='login')
def teamadmin(request):
    team = Team.objects.order_by('-id')
    context = {
            "judul": "Data Team",
            "menu":"team",
            "team_list" : team
        }
    return render(request, 'teamadmin.html', context)

@login_required(login_url='login')
def formteamadmin(request):
    if request.method == "POST":
        token_team = str(uuid.uuid4())
        #datadeskripsi = request.POST.get('deskripsi')
        form = TeamForm(request.POST, request.FILES)  # Ambil data dari request
        if form.is_valid():  # Validasi form
            team = form.save(commit=False)  
            team.token_team = token_team
            #team.deskripsi = datadeskripsi
            team.save()
            return redirect('teamadmin')  # Redirect ke halaman team setelah menyimpan
    else:
        form = TeamForm()  # Tampilkan form kosong jika GET request
    context = {
        "judul": "Form Team",
        "menu": "team",
        "form": form
    }
    return render(request, 'formteamadmin.html', context)

@login_required(login_url='login')
def editteamadmin(request, token):
    team = get_object_or_404(Team, token_team=token) #memanggil satu data yang teamnya sama maka satu yang lainnya tidak akan tertampil
    if request.method == "POST":
        form = TeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            #teamedit.deskripsi = datadeskripsi
            #teamedit.save()
            return redirect('teamadmin')  # Redirect ke halaman daftar team
    else:
        form = TeamForm(instance=team)
    context = {
        "judul": "Form Edit Team",
        "menu": "team",
        "form": form,
        'team': team
    }
    return render(request, 'formteamadmin.html', context)

@login_required(login_url='login')
def deleteteamadmin(request, token):
    team = get_object_or_404(Team, token_team=token)
    if request.method == 'POST':
        team.delete()
        return redirect('teamadmin')  
    return redirect('teamadmin')

##### INI BAGIAN MODEL INKUBASI
@login_required(login_url='login')
def modelinkubasiadmin(request):
    modelinkubasi = ModelInkubasi.objects.order_by('-id')
    context = {
            "judul": "Data ModelInkubasi",
            "menu":"modelinkubasi",
            "modelinkubasi_list" : modelinkubasi
        }
    return render(request, 'modelinkubasiadmin.html', context)

@login_required(login_url='login')
def formmodelinkubasiadmin(request):
    if request.method == "POST":
        token_modelinkubasi = str(uuid.uuid4())
        #datadeskripsi = request.POST.get('deskripsi')
        form = ModelInkubasiForm(request.POST, request.FILES)  # Ambil data dari request
        if form.is_valid():  # Validasi form
            modelinkubasi = form.save(commit=False)  
            modelinkubasi.token_modelinkubasi = token_modelinkubasi
            #modelinkubasi.deskripsi = datadeskripsi
            modelinkubasi.save()
            return redirect('modelinkubasiadmin')  # Redirect ke halaman modelinkubasi setelah menyimpan
    else:
        form = ModelInkubasiForm()  # Tampilkan form kosong jika GET request
    context = {
        "judul": "Form ModelInkubasi",
        "menu": "modelinkubasi",
        "form": form
    }
    return render(request, 'formmodelinkubasiadmin.html', context)

@login_required(login_url='login')
def editmodelinkubasiadmin(request, token):
    modelinkubasi = get_object_or_404(ModelInkubasi, token_modelinkubasi=token) #memanggil satu data yang modelinkubasinya sama maka satu yang lainnya tidak akan tertampil
    if request.method == "POST":
        form = ModelInkubasiForm(request.POST, request.FILES, instance=modelinkubasi)
        if form.is_valid():
            form.save()
            return redirect('modelinkubasiadmin')  # Redirect ke halaman daftar modelinkubasi
    else:
        form = ModelInkubasiForm(instance=modelinkubasi)
    context = {
        "judul": "Form Edit ModelInkubasi",
        "menu": "modelinkubasi",
        "form": form,
        'modelinkubasi': modelinkubasi
    }
    return render(request, 'formmodelinkubasiadmin.html', context)

@login_required(login_url='login')
def deletemodelinkubasiadmin(request, token):
    modelinkubasi = get_object_or_404(ModelInkubasi, token_modelinkubasi=token)
    if request.method == 'POST':
        modelinkubasi.delete()
        return redirect('modelinkubasiadmin')  
    return redirect('modelinkubasiadmin')

##### INI BAGIAN TESTIMONI
@login_required(login_url='login')
def testimoniadmin(request):
    testimoni = Testimoni.objects.order_by('-id')
    context = {
            "judul": "Data Testimoni",
            "menu":"testimoni",
            "testimoni_list" : testimoni
        }
    return render(request, 'testimoniadmin.html', context)

@login_required(login_url='login')
def formtestimoniadmin(request):
    if request.method == "POST":
        token_testimoni = str(uuid.uuid4())
        #datadeskripsi = request.POST.get('deskripsi')
        form = TestimoniForm(request.POST, request.FILES)  # Ambil data dari request
        if form.is_valid():  # Validasi form
            testimoni = form.save(commit=False)  
            testimoni.token_testimoni = token_testimoni
            #testimoni.deskripsi = datadeskripsi
            testimoni.save()
            return redirect('testimoniadmin')  # Redirect ke halaman testimoni setelah menyimpan
    else:
        form = TestimoniForm()  # Tampilkan form kosong jika GET request
    context = {
        "judul": "Form Testimoni",
        "menu": "testimoni",
        "form": form
    }
    return render(request, 'formtestimoniadmin.html', context)

@login_required(login_url='login')
def edittestimoniadmin(request, token):
    testimoni = get_object_or_404(Testimoni, token_testimoni=token) #memanggil satu data yang testimoninya sama maka satu yang lainnya tidak akan tertampil
    if request.method == "POST":
        form = TestimoniForm(request.POST, request.FILES, instance=testimoni)
        if form.is_valid():
            form.save()
            return redirect('testimoniadmin')  # Redirect ke halaman daftar testimoni
    else:
        form = TestimoniForm(instance=testimoni)
    context = {
        "judul": "Form Edit Testimoni",
        "menu": "testimoni",
        "form": form,
        'testimoni': testimoni
    }
    return render(request, 'formtestimoniadmin.html', context)

@login_required(login_url='login')
def deletetestimoniadmin(request, token):
    testimoni = get_object_or_404(Testimoni, token_testimoni=token)
    if request.method == 'POST':
        testimoni.delete()
        return redirect('testimoniadmin')  
    return redirect('testimoniadmin')

##### INI BAGIAN PROIL
@login_required(login_url='login')
def profiladmin(request):
    profil = Profil.objects.order_by('-id')
    context = {
            "judul": "Data Profil",
            "menu":"profil",
            "profil_list" : profil
        }
    return render(request, 'profiladmin.html', context)

@login_required(login_url='login')
def formprofiladmin(request):
    if request.method == "POST":
        token_profil = str(uuid.uuid4())
        #datadeskripsi = request.POST.get('deskripsi')
        form = ProfilForm(request.POST, request.FILES)  # Ambil data dari request
        if form.is_valid():  # Validasi form
            profil = form.save(commit=False)  
            profil.token_profil = token_profil
            #profil.deskripsi = datadeskripsi
            profil.save()
            return redirect('profiladmin')  # Redirect ke halaman profil setelah menyimpan
    else:
        form = ProfilForm()  # Tampilkan form kosong jika GET request
    context = {
        "judul": "Form Profil",
        "menu": "profil",
        "form": form
    }
    return render(request, 'formprofiladmin.html', context)
@login_required(login_url='login')
def editprofiladmin(request, token):
    profil = get_object_or_404(Profil, token_profil=token) #memanggil satu data yang profilnya sama maka satu yang lainnya tidak akan tertampil
    if request.method == "POST":
        #datadeskripsi = request.POST.get('deskripsi')
        form = ProfilForm(request.POST, request.FILES, instance=profil)
        if form.is_valid():
            form.save()
            #profiledit.deskripsi = datadeskripsi
            #profiledit.save()
            return redirect('profiladmin')  # Redirect ke halaman daftar profil
    else:
        form = ProfilForm(instance=profil)
    context = {
        "judul": "Form Edit Profil",
        "menu": "profil",
        "form": form,
        'profil': profil
    }
    return render(request, 'formprofiladmin.html', context)

@login_required(login_url='login')
def deleteprofiladmin(request, token):
    profil = get_object_or_404(Profil, token_profil=token)
    if request.method == 'POST':
        profil.delete()
        return redirect('profiladmin')  
    return redirect('profiladmin')

##### INI BAGIAN FAQ
@login_required(login_url='login')
def faqadmin(request):
    faq = Faq.objects.order_by('-id')
    context = {
            "judul": "Data Faq",
            "menu":"faq",
            "faq_list" : faq
        }
    return render(request, 'faqadmin.html', context)

@login_required(login_url='login')
def formfaqadmin(request):
    if request.method == "POST":
        token_faq = str(uuid.uuid4())
        #datadeskripsi = request.POST.get('deskripsi')
        form = FaqForm(request.POST, request.FILES)  # Ambil data dari request
        if form.is_valid():  # Validasi form
            faq = form.save(commit=False)  
            faq.token_faq = token_faq
            #faq.deskripsi = datadeskripsi
            faq.save()
            return redirect('faqadmin')  # Redirect ke halaman faq setelah menyimpan
    else:
        form = FaqForm()  # Tampilkan form kosong jika GET request
    context = {
        "judul": "Form Faq",
        "menu": "faq",
        "form": form
    }
    return render(request, 'formfaqadmin.html', context)
@login_required(login_url='login')
def editfaqadmin(request, token):
    faq = get_object_or_404(Faq, token_faq=token) #memanggil satu data yang faqnya sama maka satu yang lainnya tidak akan tertampil
    if request.method == "POST":
        #datadeskripsi = request.POST.get('deskripsi')
        form = FaqForm(request.POST, request.FILES, instance=faq)
        if form.is_valid():
            form.save()
            #faqedit.deskripsi = datadeskripsi
            #faqedit.save()
            return redirect('faqadmin')  # Redirect ke halaman daftar faq
    else:
        form = FaqForm(instance=faq)
    context = {
        "judul": "Form Edit Faq",
        "menu": "faq",
        "form": form,
        'faq': faq
    }
    return render(request, 'formfaqadmin.html', context)

@login_required(login_url='login')
def deletefaqadmin(request, token):
    faq = get_object_or_404(Faq, token_faq=token)
    if request.method == 'POST':
        faq.delete()
        return redirect('faqadmin')  
    return redirect('faqadmin')





