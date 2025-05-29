from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

class AdminPanelAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Jika bukan di admin panel, skip pengecekan
        if not request.path.startswith('/admin_panel/'):
            return self.get_response(request)
        
        # Jika user belum login, skip pengecekan (akan ditangani oleh auth middleware)
        if not request.user.is_authenticated:
            return self.get_response(request)
        
        # Cek apakah user memiliki hak akses ke admin panel
        try:
            admin_profile = request.user.admin_panel_profile
            
            # Jika mencoba mengakses user admin tapi bukan superadmin
            if not admin_profile.is_superadmin and '/auth/user/' in request.path:
                messages.error(request, 'Anda tidak memiliki akses ke halaman tersebut.')
                return redirect(reverse('admin_panel:index'))
                
        except:
            messages.error(request, 'Anda tidak memiliki akses ke admin panel.')
            return redirect(reverse('admin:index'))
        
        return self.get_response(request)