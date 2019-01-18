from django.conf import Path
from django.conf.urls import url
from django.contrib.auth import views

urlpatterns =[
    url('login', views.LoginView.as_view(template_name = 'accounts/login_form.html'), name='login')
]