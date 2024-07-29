from django.shortcuts import render, redirect
from .form import ContactForm


def homeview(request):
    return render(request, 'home.html')


def heroview(request):
    return render(request, 'hero.html')


def aboutview(request):
    return render(request, 'about.html')


def factview(request):
    return render(request, 'fact.html')


def skilsview(request):
    return render(request, 'skils.html')


def resumeview(request):
    return render(request, 'resume.html')


def protfolio(request):
    return render(request, 'protfolio.html')


def serivceview(request):
    return render(request, 'serivce.html')


def contactview(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'stform': form})
