from django.urls import path, re_path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    re_path(r'(?P<shop_id>)/order/new/', views.order_new, name='order_new'),
]
