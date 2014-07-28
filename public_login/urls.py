__author__ = 'CRogers'
from django.conf.urls import patterns, include, url
from public_login import views
urlpatterns = patterns('',
                       url(r'/^$', views.login, name="login"),
                       url(r'^login/$', views.login, name="login"),
                       url(r'^do_login', views.do_login, name="do_login"),
                       url(r'^do_logout/$', views.do_logout, name='do_logout'),
                       url(r'^register$', views.register, name="register"),
                       url(r'^createUser$', views.create_user, name="create_user"),
                       )
