from django.urls import path
from first import views

app_name = 'first'

urlpatterns = [
    path('', views.index, name='index'),
    path('connect/', views.connect, name='connect'),
    path('resume/', views.resume, name='resume'),
    path('guest/', views.guest, name='guest'),
    path('book/', views.user, name='book'),
]
