from django.conf import Path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns =[
    url('login/', auth_views.LoginView.as_view(template_name = 'accounts/login_form.html'), name='login'),
    url('signup/', views.singup, name ='signup'),
    url('profile/', views.profile, name ='profile'),

]