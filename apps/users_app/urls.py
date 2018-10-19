from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^add$', views.add),
    url(r'^delete/(?P<userid>\d+)', views.delete),
    url(r'^edit/(?P<userid>\d+)', views.edit),
    url(r'^update/(?P<userid>\d+)', views.update),
    url(r'^show/(?P<userid>\d+)', views.show),
    url(r'^goback$', views.goback),
    url(r'^gonew$', views.gonew)

]
