from django.urls import path
from . import views

app_name = 'webapp'

urlpatterns = [
    path('',views.index, name = 'index'),
    path('register',views.register, name = 'register'),
    path('logout',views.logout_request, name = 'logout'),
    path('login',views.login_request, name = 'login'),
    path('Night',views.Night, name = 'Night'),
    path('He',views.He, name = 'He'),
    path('Faith',views.Faith, name = 'Faith')
    ]
