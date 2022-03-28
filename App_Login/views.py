from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from App_Login.forms import SignUpForm

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

def sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
    dict = {'form':form, 'registered':registered}
    return render(request, 'App_Login/signup.html', context=dict)

def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None: #if user exists
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'App_Login/login.html', context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))