from .models import Pesan, Komentar

def pesan_notifications(request):
    if request.user.is_authenticated:
        belum_dibaca = Pesan.objects.filter(is_read=False, aktif=True).count()
        return {'belum_dibaca': belum_dibaca}
    return {'belum_dibaca': 0}

def komentar_notifications(request):
    if request.user.is_authenticated:
        belum_dilihat = Komentar.objects.filter(is_read=False, aktif=True).count()
        return {'belum_dilihat': belum_dilihat}
    return {'belum_dilihat': 0}
