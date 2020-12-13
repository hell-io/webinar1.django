from django.urls import path

from . import views

app_name = 'holidays'
urlpatterns = [
    path('countdown/', views.countdown, name='countdown'),
]