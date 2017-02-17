from django.conf.urls import url
from . import views

app_name = 'Transport'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^allpassengers/',views.allpassengers, name='allpassengers'),    
    url(r'^alldrivers/',views.alldrivers, name='alldrivers'),
    url(r'^allvehicles/',views.allvehicles,name='allvehicles'),    
    url(r'^passenger_details/(?P<name_id>[1-6])/$',views.passenger_details,name="passenger_details"),
    url(r'^driver_details/(?P<name_id>[1-6])/$',views.driver_details,name="driver_details"),
    url(r'^vehicle_details/(?P<name_id>[1-6])/$',views.vehicle_details,name="vehicle_details"),

]
