from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns =[
    path(r'^login/$', auth_views.LoginView.as_view(template_name = 'accounts/login_form.html'), name='login'),
    path(r'^signup/$', views.singup, name ='signup'),
    path(r'^profile/$', views.profile, name ='profile'),
    path(r'^logout/$', auth_views.LogoutView.as_view(next_page='/'), name ='logout'),

]