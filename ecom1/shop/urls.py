from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^shop/$', views.product_list, name='product_list'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^search/$', views.search, name='search'),
    url(r'^privacy-policy/$', views.privacy, name='privacy-policy'),
    url(r'^return-policy/$', views.PolicyReturn, name='return-policy'),
    url(r'^Shipment/$', views.Shipment, name='Shipment'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]

