from django.shortcuts import render


def login(request):
    context = {}
    return render(request, 'home.html', context)


def signup(request):
    context = {}
    return render(request, 'createaccount.html', context)


def modifyaccount(request, id_user):
    context = {'id_user': id_user}
    return render(request, 'modifyaccount.html')
