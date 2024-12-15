from django.shortcuts import render
from .models import Sign_Up
# Create your views here.
def index(request):
    user=request.POST.get('username')
    email=request.POST.get('email')
    password=request.POST.get('password')
    check=request.POST.get('checkbox')
    data=Sign_Up(username=user,email=email,password=password,checkbox=check)
    data.save()

    return render(request,'index.html')