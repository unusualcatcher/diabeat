from django.urls import path
from .views import health, form

urlpatterns = [
    path('', health, name='health'),
    path('form/', form, name='form')
]