from rest_framework import serializers

from rv.models import  User, Rv, Personne, Patient

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username',  'password')


class SerializerCreatePatient(serializers.ModelSerializer):

    class Meta:
        model=Patient
        fields=('first_name','last_name','email','phone','age','address')
       

class PersonneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Personne
        fields=('name','age')


class CreateRvSerializer(serializers.ModelSerializer):

    class Meta:
        model=Rv
        fields=('title','patient','email','date','hours','place','hello')

    
    