# snippets/urls.py
from django.conf.urls import url
from snippets import views

urlpatterns = [
     url(r'^$', views.home, name='home'),

    url(r'^detail/(?P<snippet_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add, name="add"),
    url(r'^delete_snippet/(?P<pk>\d+)$', views.delete_snippet, name="delete_snippet"),

]
