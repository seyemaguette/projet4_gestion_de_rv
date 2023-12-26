from django.contrib import admin
from .models import User, Doctor, Profil, Patient, Rv
from django.contrib.auth.admin import UserAdmin

# Register your models here.
    
admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Profil)
admin.site.register(Patient)
admin.site.register(Rv)

