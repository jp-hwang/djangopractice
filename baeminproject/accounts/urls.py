from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns =[
    path('login/', auth_views.LoginView.as_view(template_name = 'accounts/login_form.html'), name='login'),
    path('signup/', views.singup, name ='signup'),
    path('profile/', views.profile, name ='profile'),

]