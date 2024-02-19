from django.shortcuts import render
from flask import request
from rest_framework import generics

from .models import Pelicula, IsAuthenticatedorReadOnly
from .serializers import PeliculaSerializer


# Create your views here.

class ListaPeliculas(generics.ListCreateAPIView):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    permission_classes = [IsAuthenticatedorReadOnly]

class DetallesPelicula(generics.RetrieveDestroyAPIView):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

class registro(request):
    if request.methond == 'POST':
        email = request.Post['email']
        password = request.Post['password']
        first_name = request.Post['first_name']