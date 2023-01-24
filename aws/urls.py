from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('upload form/', views.model_form_upload, name='model_form_upload'),

]