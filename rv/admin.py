from django.contrib import admin
from .models import Personne,User, Doctor, Profil, Patient, Rv
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.authtoken.admin import TokenAdmin

# Register your models here.
    
admin.AdminSite(TokenAdmin)
admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Profil)
admin.site.register(Patient)
admin.site.register(Rv)
admin.site.register(Personne)

