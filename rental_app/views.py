from django.shortcuts import render, redirect
from .models import Customer, Car, Provider, Feedback


def register_page(request):
    return render(request, "provider_register.html")
