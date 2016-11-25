from django.conf.urls import url
from web.views import *

urlpatterns = [
    #Login-Logout Functionality
    # url(r'^login', Login, name='login'),
    # url(r'^logout', Logout, name='logout'),
    url(r'^test', Test),
    ]
