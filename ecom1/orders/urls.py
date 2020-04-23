from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^charge/(?P<id>\d+)/$', views.charge, name='charge'),
    # url(r'^checkout/$', views.checkout_page, name='checkout'),
    # url(r'^payment/$', views.payment, name='payment'),
    # url(r'^money/$', views.view_that_asks_for_money, name='money')
]