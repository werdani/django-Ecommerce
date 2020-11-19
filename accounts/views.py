from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth import login , authenticate
from .models import Profile
from . forms import UserForm,ProfileForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user =authenticate(username=username,password=password)
            login(request,user)
            return redirect('/')

    else:
        form = UserCreationForm()

    return render(request,'registration/signup.html',{'form':form})


        