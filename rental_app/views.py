from django.shortcuts import render,redirect
from .models import User,Customer,Car,Provider,Feedback

def register_page(request):
    return render(request,"register.html")
