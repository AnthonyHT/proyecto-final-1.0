from django.db import models
from rest_framework import permissions


# Create your models here.

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    anio_lanzamiento = models.IntegerField()
    genero = models.CharField(max_length=50)

class IsAuthenticatedorReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

class CustomUserManager(BaseUserManager):
    def create_user(selfself):
        