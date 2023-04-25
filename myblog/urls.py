from django.urls import path
from . import views

urlpatterns = [
   path('', views.index),
   path('information/', views.information),
   path('post/', views.post),
   path('contact/', views.contact),
]