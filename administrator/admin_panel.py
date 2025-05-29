from django.contrib.admin import AdminSite
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import MenuPilihan, AdminPanelUser
from .admin import MenuPilihanAdmin, CustomUserAdmin

class AdminPanelSite(AdminSite):
    site_header = 'Admin Panel'
    site_title = 'Admin Panel'
    index_title = 'Dashboard Admin Panel'
    
    def has_permission(self, request):
        # Cek apakah user memiliki akses ke admin panel
        if not request.user.is_authenticated:
            return False
        
        # Cek apakah user adalah admin panel user
        try:
            admin_profile = request.user.admin_panel_profile
            return True
        except AdminPanelUser.DoesNotExist:
            return False

admin_panel_site = AdminPanelSite(name='admin_panel')

# Register models ke admin panel
admin_panel_site.register(MenuPilihan, MenuPilihanAdmin)
admin_panel_site.register(User, CustomUserAdmin)