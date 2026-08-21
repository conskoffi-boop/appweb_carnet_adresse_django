from django.shortcuts import render,redirect
from .models import User,Compte
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout



def inscription (request):

    if request.method == 'POST':
        username =request.POST.get('username')
        prenom=request.POST.get('prenom')
        email = request.POST.get('email')
        password = request.POST.get('password')
        telephone = request.POST.get('telephone')

        if User.objects.filter(email=email).exists():
            messages.error(request , 'cet email est deja ratacher a un compte ')
            return redirect('auth')


        new_user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
        )

        Compte.objects.create(
            username = username,
            prenom=prenom,
            email=email,
            telephone=telephone,
             )
        return redirect('index')

    return render (request,'auth.html')


 

 
def connexion (request):
    if request.method == 'POST':
        username = request.POST.get('login-username')
        password = request.POST.get('login-password')

        User = authenticate(
            request, 
            username=username,
            password=password,
        )

        if User is None:
            messages.error(request , 'email ou mot de passe incorect')
            return redirect('auth')

        if User is not None :
           
            login(request,User)

            return redirect('index')

    return render(request , 'auth.html')


def deconnexion (request):
    logout(request)
    return render(request,'auth.html')
    
