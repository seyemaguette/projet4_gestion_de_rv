from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Doctor, Role, Profil, Patient,Rv
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator


from django.core.exceptions import ValidationError

class UserCreation(UserCreationForm):

   
   
    first_name=forms.CharField(label='Prenom',required=True)
    last_name=forms.CharField(label='Nom',required=True)
    email=forms.EmailField(label='Email',required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email Already Exists')

        return email
    
    username = forms.CharField(
        label = 'Nom d"utilisateur',
        widget=forms.TextInput(
            attrs={
    
                "class": "form-control"}))

    password1 = forms.CharField(
       label = 'Mot de passe',       
       widget=forms.PasswordInput(
            attrs={
                "class": "form-control"})) 
    password2 = forms.CharField(
       label = 'Confirmation du mot de passe',       
       widget=forms.PasswordInput(
            attrs={
                "class": "form-control"}))
    
    class Meta(UserCreationForm.Meta):
        
        model= User
        fields= ('username','email','first_name','last_name',
                 )
   



class UserupdateForm(forms.ModelForm):

    email=forms.EmailField(label='Email')
    username = forms.CharField(
        label = 'Nom d"utilisateur',
        widget=forms.TextInput(
            attrs={
    
                "class": "form-control"}))

    class Meta():
        model = User
        fields= ('username','email',)


class DoctorForm(forms.ModelForm):
    role=forms.ChoiceField(label='Fonction',choices=Role)



    
   
    class Meta:
        model=Doctor
        fields=('address','phone','role')
        widgets = {                         
            'phone': PhoneNumberPrefixWidget(initial='SN',),
        }

        
class UpdateDoctorForm(forms.ModelForm):
   
   
    class Meta:
        model=Doctor
        fields=('address','phone')



class UpdateProfil(forms.ModelForm):
   
   
    class Meta:
        model=Profil
        fields=['avatar']



class CreatePatient(forms.ModelForm):

    class Meta:
        model=Patient
        fields=('first_name','last_name','email','phone','age','address',)
        widgets = {                         
            'phone': PhoneNumberPrefixWidget(initial='SN',),
        }


class CreateRv(forms.ModelForm):
    # date= forms.DateField(label='Date', widget=forms.DateInput())

    class Meta:
        model=Rv
        fields=('title','patient','email','date','hours','place',)

     
   


    

class login_form(forms.Form):
    username = forms.CharField(
        label = 'Nom d"utilisateur',
        widget=forms.TextInput(
            attrs={
                "class": "form-control"}))
    password = forms.CharField(
       label = 'Mot de passe',       
       widget=forms.PasswordInput(
            attrs={
                "class": "form-control"}))

    

 
    



# class Doctorsignup(UserCreationForm):
  
#     username = forms.CharField(
#         label = 'Nom d"utilisateur',
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control"}))
#     password1 = forms.CharField(
#        label = 'Mot de passe',       
#        widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"})) 
#     password2 = forms.CharField(
#        label = 'Confirmation du mot de passe',       
#        widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"}))
#     is_doctor=forms.BooleanField(label='',widget=forms.HiddenInput() ,initial=True)
    
#     class Meta():
        
#         model= Doctor
#         fields= ('username','profil','first_name','last_name','email',
#                 'phone','address','role','password1' ,'password2','is_doctor')

# class Doctorupdate(PasswordChangeForm):
#     # username = forms.CharField(
#     #     label = 'Nom d"utilisateur',
#     #     widget=forms.HiddenInput(
#     #         attrs={
#     #             "class": "form-control"}))
#     password = forms.CharField(
#        label = 'Nouveau mot de passe',       
#        widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"})) 
#     password1 = forms.CharField(
#        label = 'Mot de passe',       
#        widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"})) 
    
#     password2 = forms.CharField(
#        label = 'Confirmation du mot de passe',       
#        widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"}))
#     is_doctor=forms.BooleanField(label='',widget=forms.HiddenInput() ,initial=True)
    
#     class Meta():
        
#         model= Doctor
#         fields= ('profil','first_name','last_name','email',
#                 'phone','address','password1' ,'password2','is_doctor')
        

        



