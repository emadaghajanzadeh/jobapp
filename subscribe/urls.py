from django.urls import path, include
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name = 'subscribe'),
    path('thank_you/', views.thank_you, name = "thank_you")

]
