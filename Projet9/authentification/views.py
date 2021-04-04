from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import CreateUserForm

def login(request):
    form = CreateUserForm()
    context = {'form': form}
    return render(request, 'home.html', context)


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Le compte a été créé au nom de :" + user)
            return redirect('account')

    context = {'form': form}
    return render(request, 'createaccount.html', context)


def modifyaccount(request, id_user):
    context = {'id_user': id_user}
    return render(request, 'modifyaccount.html')
