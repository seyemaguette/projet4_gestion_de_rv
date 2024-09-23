from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save
# from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

from PIL import Image


Role=(
        (  '' ,'' ),
        (  'cardiologue' ,'cardiologue' ),
        (  'dermatologue' ,'dermatologue' ),
        (  'gynecologue' ,'gynecologue' ),
        (  'generaliste' ,'generaliste' ),
        (  'dentiste' ,'dentiste' ),
        (  'neurologue' ,'neurologue' ),
        (  'pediatre' ,'pediatre' ),
        (  'psychiatre' ,'psychiatre' ),
    )
   


class Personne(models.Model):
   
    
    name=models.CharField(verbose_name=("name"),  max_length=20,)
    age=models.CharField(verbose_name=("age"),  max_length=16,)
 
         
    def __str__(self):
        return self.name
    

class User(AbstractUser):
    email=models.EmailField(unique=True,null=True)
    first_name=models.CharField(  max_length=100,null=True, )
    last_name=models.CharField(  max_length=100,null=True,)
    
    is_doctor=models.BooleanField(default=False)
    
    




class Doctor(models.Model):
   
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name='doctor')
    
    address=models.CharField(verbose_name=("Adresse"),  max_length=20,)
    phone=models.CharField(verbose_name=("Telephone"),  max_length=16,)

    role=models.CharField( verbose_name=("Fonction"),choices=Role, max_length=20,)
    
    @receiver(post_save,sender=User)
    def create_doctor(sender,instance, created,**kwargs):
            if created:
                    Doctor.objects.get_or_create(user=instance)
                
        

    @receiver(post_save,sender=User)
    def save_doctor(sender,instance, **kwargs):
            instance.doctor.save()

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}   '
    
        


class Profil(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    avatar=models.ImageField(verbose_name='Photo', upload_to='images/',blank=True,default='images/avatar.png')


    @receiver(post_save,sender=User)
    def create_profil(sender,instance, created,**kwargs):
            if created:
                    Profil.objects.get_or_create(user=instance)
                
        

    @receiver(post_save,sender=User)
    def save_profil(sender,instance, **kwargs):
            instance.profil.save()


    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} '
    
    
    


class Patient(models.Model):
      
    first_name=models.CharField(verbose_name='Prenom',max_length=60)
    last_name=models.CharField(verbose_name='Nom',max_length=60)
    age= models.PositiveIntegerField ()
    address=models.CharField(verbose_name=("Adresse"),  max_length=20,)
    phone=models.CharField(verbose_name=("Telephone"),  max_length=16,null=True)
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    archive=models.BooleanField(default=False)
    email=models.EmailField(unique=True,null=True)
      
      
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
      
    



class Rv(models.Model):
        title=models.CharField( verbose_name='Titre', max_length=50)
        patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
        # patient=models.CharField( verbose_name='Avec Qui', max_length=50)
        email=models.EmailField( verbose_name='Email',null=True)
        date=models.DateField( verbose_name= 'Date')
        hours= models.TimeField(  verbose_name='Heure' )
        place= models.CharField( verbose_name= 'Lieu',max_length=50, )
        doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
        archive=models.BooleanField(default=False)

        def __str__(self):
             return f'{self.title} '
        
        
        def hello(self) :
          return "bonjour"

        