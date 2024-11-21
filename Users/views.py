from django.shortcuts import render

# Create your views here.
from dj_rest_auth.registration.views import RegisterView
from .Serializers import CustomSerializer


class CustomRegisterView(RegisterView):
    serializer_class = CustomSerializer