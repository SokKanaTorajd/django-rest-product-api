from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Product, User
from .serializers import UserSerializer, ProductSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class CustomTokenObtainPairView(TokenObtainPairView):
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]
    permission_classes = [permissions.AllowAny]

# class LoginView(TokenObtainPairView):
#     permission_classes = [permissions.AllowAny]

class ListProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class DetailProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

