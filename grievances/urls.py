from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.grievance_detail, name='grievance_detail'),
    url(r'^new/$', views.grievance_new, name='grievance_new'),
    url(r'^signup/$', views.sign_up, name='sign_up'),
    url(r'^login/$', views.login, name='login'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^council_team/$', views.council_team, name='council_team'),



]