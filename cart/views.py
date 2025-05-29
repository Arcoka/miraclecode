from django.shortcuts import render, get_object_or_404, redirect
from .models import SlidePenjualan, Pemesanan, Jasa, KategoriPenjualan, Produk
from .forms import SlidePenjualanForm, PemesananForm, JasaForm, KategoriPenjualanForm, ProdukForm
import uuid
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def berandapenjualan(request): 
    slidepenjualan = SlidePenjualan.objects.filter(aktif=True).count()
    # pemesanan = Pemesanan.objects.filter(aktif=True).count()
    jasa = Jasa.objects.filter(aktif=True).count()
    # kategoripenjualan = KategoriPenjualan.objects.filter(aktif=True).count()
    # produk = Produk.objects.filter(aktif=True).count()
    
    isi = {
        "judul": "Administrator Cart",
        # 'berita':berita,
        'slidepenjualan':slidepenjualan,
        # 'pemesanan':pemesanan, #agar terbaca di dashboard
        'jasa':jasa
        # 'kategoripenjualan':kategoripenjualan,
        # 'produk':produk,
        # 'menu':berandaadmin,
        
    } 
    return render(request, 'berandapenjualan.html', isi)

##### INI BAGIAN SLIDEPENJUALAN
@login_required(login_url='login')
def slidepenjualanadmin(request):
    slidepenjualan = SlidePenjualan.objects.order_by('-id')
    context = {
            "judul": "Data SlidePenjualan",
            "menu":"slidepenjualan",
            "slidepenjualan_list" : slidepenjualan
        }
    return render(request, 'slidepenjualanadmin.html', context)

@login_required(login_url='login')
def formslidepenjualanadmin(request):
    if request.method == "POST":
        token_slidepenjualan = str(uuid.uuid4())
        #datadeskripsi = request.POST.get('deskripsi')
        form = SlidePenjualanForm(request.POST, request.FILES)  # Ambil data dari request
        if form.is_valid():  # Validasi form
            slidepenjualan = form.save(commit=False)  
            slidepenjualan.token_slidepenjualan = token_slidepenjualan
            #slidepenjualan.deskripsi = datadeskripsi
            slidepenjualan.save()
            return redirect('slidepenjualanadmin')  # Redirect ke halaman slidepenjualan setelah menyimpan
    else:
        form = SlidePenjualanForm()  # Tampilkan form kosong jika GET request
    context = {
        "judul": "Form SlidePenjualan",
        "menu": "slidepenjualan",
        "form": form
    }
    return render(request, 'formslidepenjualanadmin.html', context)

@login_required(login_url='login')
def editslidepenjualanadmin(request, token):
    slidepenjualan = get_object_or_404(SlidePenjualan, token_slidepenjualan=token) #memanggil satu data yang slidepenjualannya sama maka satu yang lainnya tidak akan tertampil
    if request.method == "POST":
        form = SlidePenjualanForm(request.POST, request.FILES, instance=slidepenjualan)
        if form.is_valid():
            form.save()
            #slidepenjualanedit.deskripsi = datadeskripsi
            #slidepenjualanedit.save()
            return redirect('slidepenjualanadmin')  # Redirect ke halaman daftar slidepenjualan
    else:
        form = SlidePenjualanForm(instance=slidepenjualan)
    context = {
        "judul": "Form Edit SlidePenjualan",
        "menu": "slidepenjualan",
        "form": form,
        'slidepenjualan': slidepenjualan
    }
    return render(request, 'formslidepenjualanadmin.html', context)

@login_required(login_url='login')
def deleteslidepenjualanadmin(request, token):
    slidepenjualan = get_object_or_404(SlidePenjualan, token_slidepenjualan=token)
    if request.method == 'POST':
        slidepenjualan.delete()
        return redirect('slidepenjualanadmin')  
    return redirect('slidepenjualanadmin')

##### INI BAGIAN PEMESANAN
@login_required(login_url='login')
def pemesananadmin(request):
    pemesanan = Pemesanan.objects.order_by('-id')
    context = {
            "judul": "Data Pemesanan",
            "menu":"pemesanan",
            "pemesanan_list" : pemesanan
        }
    return render(request, 'pemesananadmin.html', context)

@login_required(login_url='login')
def formpemesananadmin(request):
    if request.method == "POST":
        token_pemesanan = str(uuid.uuid4())
        #datadeskripsi = request.POST.get('deskripsi')
        form = PemesananForm(request.POST, request.FILES)  # Ambil data dari request
        if form.is_valid():  # Validasi form
            pemesanan = form.save(commit=False)  
            pemesanan.token_pemesanan = token_pemesanan
            #pemesanan.deskripsi = datadeskripsi
            pemesanan.save()
            return redirect('pemesananadmin')  # Redirect ke halaman pemesanan setelah menyimpan
    else:
        form = PemesananForm()  # Tampilkan form kosong jika GET request
    context = {
        "judul": "Form Pemesanan",
        "menu": "pemesanan",
        "form": form
    }
    return render(request, 'formspemesananadmin.html', context)
    
@login_required(login_url='login')
def editpemesananadmin(request, token):
    pemesanan = get_object_or_404(Pemesanan, token_pemesanan=token) #memanggil satu data yang pemesanannya sama maka satu yang lainnya tidak akan tertampil
    if request.method == "POST":
        form = PemesananForm(request.POST, request.FILES, instance=pemesanan)
        if form.is_valid():
            form.save()
            #pemesananedit.deskripsi = datadeskripsi
            #pemesananedit.save()
            return redirect('pemesananadmin')  # Redirect ke halaman daftar pemesanan
    else:
        form = PemesananForm(instance=pemesanan)
    context = {
        "judul": "Form Edit Pemesanan",
        "menu": "pemesanan",
        "form": form,
        'pemesanan': pemesanan
    }
    return render(request, 'formspemesananadmin.html', context)

@login_required(login_url='login')
def deletepemesananadmin(request, token):
    pemesanan = get_object_or_404(Pemesanan, token_pemesanan=token)
    if request.method == 'POST':
        pemesanan.delete()
        return redirect('pemesananadmin')  
    return redirect('pemesananadmin')


##### INI BAGIAN PRODUK POPULER
@login_required(login_url='login')
def jasaadmin(request):
    jasa = Jasa.objects.order_by('-id')
    context = {
            "judul": "Data Jasa",
            "menu":"jasa",
            "jasa_list" : jasa
        }
    return render(request, 'jasaadmin.html', context)

@login_required(login_url='login')
def formjasaadmin(request):
    if request.method == "POST":
        token_jasa = str(uuid.uuid4())
        #datadeskripsi = request.POST.get('deskripsi')
        form = JasaForm(request.POST, request.FILES)  # Ambil data dari request
        if form.is_valid():  # Validasi form
            jasa = form.save(commit=False)  
            jasa.token_jasa = token_jasa
            #jasa.deskripsi = datadeskripsi
            jasa.save()
            return redirect('jasaadmin')  # Redirect ke halaman jasa setelah menyimpan
    else:
        form = JasaForm()  # Tampilkan form kosong jika GET request
    context = {
        "judul": "Form Jasa",
        "menu": "jasa",
        "form": form
    }
    return render(request, 'formjasaadmin.html', context)

@login_required(login_url='login')
def editjasaadmin(request, token):
    jasa = get_object_or_404(Jasa, token_jasa=token) #memanggil satu data yang jasanya sama maka satu yang lainnya tidak akan tertampil
    if request.method == "POST":
        form = JasaForm(request.POST, request.FILES, instance=jasa)
        if form.is_valid():
            form.save()
            #jasaedit.deskripsi = datadeskripsi
            #jasaedit.save()
            return redirect('jasaadmin')  # Redirect ke halaman daftar jasa
    else:
        form = JasaForm(instance=jasa)
    context = {
        "judul": "Form Edit Jasa",
        "menu": "jasa",
        "form": form,
        'jasa': jasa
    }
    return render(request, 'formjasaadmin.html', context)

@login_required(login_url='login')
def deletejasaadmin(request, token):
    jasa = get_object_or_404(Jasa, token_jasa=token)
    if request.method == 'POST':
        jasa.delete()
        return redirect('jasaadmin')  
    return redirect('jasaadmin')


####### INI BAGIAN KATEGORIPENJUALAN
@login_required(login_url='login')
def kategoripenjualanadmin(request):
    kategoripenjualan = KategoriPenjualan.objects.order_by('-id')
    context = {
            "judul": "Data KategoriPenjualan",
            "menu":"kategoripenjualan",
            "kategoripenjualan_list" : kategoripenjualan
        }
    return render(request, 'kategoripenjualanadmin.html', context)

@login_required(login_url='login')
def formkategoripenjualanadmin(request):
    if request.method == "POST":
        token_kategoripenjualan = str(uuid.uuid4())
        datadeskripsi = request.POST.get('deskripsi')
        form = KategoriPenjualanForm(request.POST, request.FILES)  # Ambil data dari request
        if form.is_valid():  # Validasi form
            kategoripenjualan = form.save(commit=False)  
            kategoripenjualan.token_kategoripenjualan = token_kategoripenjualan
            kategoripenjualan.deskripsi = datadeskripsi
            kategoripenjualan.save()
            return redirect('kategoripenjualanadmin')  # Redirect ke halaman kategoripenjualan setelah menyimpan
    else:
        form = KategoriPenjualanForm()  # Tampilkan form kosong jika GET request
    context = {
        "judul": "Form KategoriPenjualan",
        "menu": "kategoripenjualan",
        "form": form
    }
    return render(request, 'formkategoripenjualanadmin.html', context)

@login_required(login_url='login')
def editkategoripenjualanadmin(request, token):
    kategoripenjualan = get_object_or_404(KategoriPenjualan, token_kategoripenjualan=token) #memanggil satu data yang kategoripenjualannya sama maka satu yang lainnya tidak akan tertampil
    if request.method == "POST":
        datadeskripsi = request.POST.get('deskripsi')
        form = KategoriPenjualanForm(request.POST, request.FILES, instance=kategoripenjualan)
        if form.is_valid():
            kategoripenjualanedit = form.save(commit=False)
            kategoripenjualanedit.deskripsi = datadeskripsi
            kategoripenjualanedit.save()
            return redirect('kategoripenjualanadmin')  # Redirect ke halaman daftar kategoripenjualan
    else:
        form = KategoriPenjualanForm(instance=kategoripenjualan)
    context = {
        "judul": "Form Edit KategoriPenjualan",
        "menu": "kategoripenjualan",
        "form": form,
        'kategoripenjualan': kategoripenjualan
    }
    return render(request, 'formkategoripenjualanadmin.html', context)

@login_required(login_url='login')
def deletekategoripenjualanadmin(request, token):
    kategoripenjualan = get_object_or_404(KategoriPenjualan, token_kategoripenjualan=token)
    if request.method == 'POST':
        kategoripenjualan.delete()
        return redirect('kategoripenjualanadmin')  
    return redirect('kategoripenjualanadmin')

########  INI BAGIAN PRODUK

# @login_required(login_url='login')
# def produkadmin(request):
#     produk = Produk.objects.order_by('-id')
#     context = {
#             "judul": "Data Produk",
#             "menu":"produk",
#             "produk_list" : produk
#         }
#     return render(request, 'produkadmin.html', context)

# @login_required(login_url='login')
# def formprodukadmin(request):
#     if request.method == "POST":
#         token_produk = str(uuid.uuid4())
#         #datadeskripsi = request.POST.get('deskripsi')
#         form = ProdukForm(request.POST, request.FILES)  # Ambil data dari request
#         if form.is_valid():  # Validasi form
#             produk = form.save(commit=False)  
#             produk.token_produk = token_produk
#             #produk.deskripsi = datadeskripsi
#             produk.save()
#             return redirect('produkadmin')  # Redirect ke halaman produk setelah menyimpan
#     else:
#         form = ProdukForm()  # Tampilkan form kosong jika GET request
#     context = {
#         "judul": "Form Produk",
#         "menu": "produk",
#         "form": form
#     }
#     return render(request, 'formprodukadmin.html', context)

# @login_required(login_url='login')
# def editprodukadmin(request, token):
    produk = get_object_or_404(Produk, token_produk=token) #memanggil satu data yang produknya sama maka satu yang lainnya tidak akan tertampil
    if request.method == "POST":
        #datadeskripsi = request.POST.get('deskripsi')
        form = ProdukForm(request.POST, request.FILES, instance=produk)
        if form.is_valid():
            form.save()
            #produkedit.deskripsi = datadeskripsi
            #produkedit.save()
            return redirect('produkadmin')  # Redirect ke halaman daftar produk
    else:
        form = ProdukForm(instance=produk)
    context = {
        "judul": "Form Edit Produk",
        "menu": "produk",
        "form": form,
        'produk': produk
    }
    return render(request, 'formprodukadmin.html', context)

# @login_required(login_url='login')
# def deleteprodukadmin(request, token):
#     produk = get_object_or_404(Produk, token_produk=token)
#     if request.method == 'POST':
#         produk.delete()
#         return redirect('produkadmin')  
#     return redirect('produkadmin')


# View untuk menampilkan halaman produk yang bisa difilter
@login_required(login_url='login')
def produkdisplay(request):
    produk = Produk.objects.filter(aktif=True)
    kategoripenjualan = KategoriPenjualan.objects.filter(aktif=True)
    
    context = {
        'produk': produk,
        'kategoripenjualan': kategoripenjualan,
    }
    return render(request, 'produkdisplay.html', context) 

# View untuk admin produk
def produkadmin(request):
    produk = Produk.objects.all()
    kategoripenjualan = KategoriPenjualan.objects.filter(aktif=True)
    
    context = {
        'produk': produk,
        'kategoripenjualan': kategoripenjualan,
    }
    return render(request, 'produkadmin.html', context)

# View untuk form tambah produk
@login_required(login_url='login')
def formprodukadmin(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        deskripsi = request.POST.get('deskripsi')
        harga = request.POST.get('harga')
        kategori_id = request.POST.get('kategori')
        gambar = request.FILES.get('gambar')
        aktif = request.POST.get('aktif', False) == 'on'  # Checkbox handling
        
        # Generate token unik
        token = str(uuid.uuid4())
        
        # Ambil kategori
        kategoripenjualan = get_object_or_404(KategoriPenjualan, id=kategori_id) if kategori_id else None
        
        # Buat objek produk baru
        produk = Produk.objects.create(
            nama=nama,
            deskripsi=deskripsi,
            harga=harga,
            kategoripenjualan=kategoripenjualan,
            gambar=gambar,
            aktif=aktif,
            token_produk=token
        )
        
        return redirect('produkadmin')
    
    kategoripenjualan = KategoriPenjualan.objects.filter(aktif=True)
    context = {
        'kategoripenjualan': kategoripenjualan,
    }
    return render(request, 'formprodukadmin.html', context)

# View untuk edit produk
@login_required(login_url='login')
def editprodukadmin(request, token):
    produk = get_object_or_404(Produk, token_produk=token)
    kategoripenjualan = KategoriPenjualan.objects.filter(aktif=True)
    
    if request.method == 'POST':
        nama = request.POST.get('nama')
        deskripsi = request.POST.get('deskripsi')
        harga = request.POST.get('harga')
        kategori_id = request.POST.get('kategori')
        gambar = request.FILES.get('gambar')
        aktif = request.POST.get('aktif', False) == 'on'  # Checkbox handling
        
        # Update data produk
        produk.nama = nama
        produk.deskripsi = deskripsi
        produk.harga = harga
        produk.aktif = aktif
        if kategori_id:
            produk.kategoripenjualan = get_object_or_404(KategoriPenjualan, id=kategori_id)
        if gambar:
            produk.gambar = gambar
            
        produk.save()
        return redirect('produkadmin')
    
    context = {
        'produk': produk,
        'kategoripenjualan': kategoripenjualan,
    }
    return render(request, 'editprodukadmin.html', context)

# View untuk menghapus produk
@login_required(login_url='login')
def deleteprodukadmin(request, token):
    produk = get_object_or_404(Produk, token_produk=token)
    produk.delete()
    return redirect('produkadmin')


