from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^start$', views.index, name='index'),
    url(r'^contact$', views.contact, name='contact')
]
