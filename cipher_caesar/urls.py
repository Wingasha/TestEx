from django.conf.urls import url

from . import views

app_name = 'cipher_caesar'
urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^decode/$', views.decode, name='decode'),
    url(r'^encode/$', views.encode, name='encode'),
]