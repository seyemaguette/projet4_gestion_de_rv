from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LogoutView
from .views import( dashboard, index,my_account,new_doctor, login_view, update_password,logout_doctor, update_doctor,update_profil
, create_patient, list_patients, details_patients, delete_patient,update_patient, create_rv, list_rv,delete_rv,
details_rv, update_rv,api_view)

urlpatterns = [
      
    #---------------------api-------------------
    path('', index,name='index'),
    path('dashboard/', dashboard,name='dashboard'),
    path('my_account/', my_account,name='my_account'),
    path('new_doctor/', new_doctor,name='new_doctor'),
    path('login/',login_view, name='login'),
    path('update_password/',update_password, name='update_password'),
    path('update_doctor/',update_doctor, name='update_doctor'),
    path('update_profil/',update_profil, name='update_profil'),
    path('logout/', logout_doctor ,name='logout'),
    path('create_patient/', create_patient ,name='create_patient'),
    path('list_patients/', list_patients ,name='list_patients'),
    path('details_patients/<int:id>', details_patients ,name='details_patients'),
    path('delete_patient/<int:id>', delete_patient ,name='delete_patient'),
    path('update_patient/<int:id>', update_patient ,name='update_patient'),
    path('create_rv/', create_rv ,name='create_rv'),
    path('list_rv/', list_rv ,name='list_rv'),
    path('details_rv/<int:id>', details_rv ,name='details_rv'),
    path('delete_rv/<int:id>', delete_rv ,name='delete_rv'),
    path('update_rv/<int:id>', update_rv ,name='update_rv'),
    # path('update_rv/<int:id>', update_rv ,name='update_rv'),
]
