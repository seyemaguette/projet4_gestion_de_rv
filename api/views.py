from django.shortcuts import render
from .serializer import UserSerializer,PersonneSerializer,SerializerCreatePatient
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import generics, mixins, permissions, authentication, viewsets
from rv.models import Patient,Doctor,Rv,Personne
from rest_framework.authtoken.models import Token
# Create your views here.
#------------------------API------------------ 
 #_________________________USERS____________________________
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserLoginView(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
 #---------------PATIENTS---------------
class SerializerCreatePatient(generics.ListCreateAPIView):
    
    queryset= Patient.objects.all()
    serializer_class = SerializerCreatePatient
    # authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes= [permissions.IsAuthenticated,permissions.IsAuthenticatedOrReadOnly]


    def get_queryset(self):
            """
            This view should return a list of all the purchases
            for the currently authenticated user.
            """
            user = self.request.user
            return Patient.objects.filter(doctor__user=user)


    def perform_create(self, serializer):
        user =self.request.user
        doc = Doctor.objects.get(user=user)
        serializer.save(doctor=doc )
    
 