from django.urls import path

from portfolio import views

urlpatterns = [
    path('index/', views.profile, name='index'),

]
