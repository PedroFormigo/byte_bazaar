from django.urls import path

from .views import homepage, about, contacts

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about', about, name='about'),
    path('contacts', contacts, name='contacts'),
]
