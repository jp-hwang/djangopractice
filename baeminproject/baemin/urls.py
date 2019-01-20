from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('(?P<shop_id>\d+)/order/new/$', views.order_new, name='order_new'),
]
