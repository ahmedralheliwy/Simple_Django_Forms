from django.shortcuts import render,HttpResponse
from .models import Sign_Up
from .forms import Sign_UpForm
# Create your views here.
def index(request):
    if request.method=='POST':
        data=Sign_UpForm(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse("Successful send data.")
        return render(request,'index.html',{'form':data})
    else:
        form=Sign_UpForm(None)
        return render(request,'index.html',{'form':form})
