from django.shortcuts import render
from django.http import HttpResponse
from .models import Sign_Up
from .forms import Sign_UpForm
# Create your views here.
def index(request):
    if request.method=='POST':
        data=Sign_UpForm(request.POST)
        if data.is_valid():
            data.save()
    return render(request,'index.html',{'tem_form':Sign_UpForm})