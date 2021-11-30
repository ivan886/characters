from django.shortcuts import render, redirect
from django.http import HttpResponse
from characters.models import Universe
# Create your views here.



from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_v(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username,password=password)
        print(" : )",user)

        if user:
            login(request,user)
            return redirect('/characters')
        else:
             return render(request,'users/login.html',{'error':'invalid username or password'})
    return render(request,'users/login.html')
