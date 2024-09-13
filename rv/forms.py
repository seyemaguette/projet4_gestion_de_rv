from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Personne,User, Doctor, Role, Profil, Patient,Rv
# from phonenumber_field.widgets import PhoneNumberPrefixWidget
# from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError

class PersonneForm(forms.ModelForm):
    class Meta:
        model=Personne
        fields=('name','age')

     


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
        # widgets = {                         
        #     'phone': forms.CharField(label='SN',),
        # }

        
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
        

class CreateRv(forms.ModelForm):

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

    

 
    



