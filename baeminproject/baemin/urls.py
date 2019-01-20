from django.urls import path
from . import views

urlpatterns = [
    path(r'^$', views.index, name='index'),
    path(r'^(?P<int:shop_id>\d+)/order/new/$', views.order_new, name='order_new'),
]
