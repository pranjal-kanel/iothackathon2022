from django.urls import path

from . import views

urlpatterns = [
    path('writecard', views.writeCard, name='writecard'),
    path('readcard', views.readCard, name='readcard')
]