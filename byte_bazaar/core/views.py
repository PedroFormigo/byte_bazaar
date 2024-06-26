from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'core/homepage.html', {})

def about(request):
    return render(request, 'core/about.html', {})

def contacts(request):
    return render(request, 'core/contacts.html', {})