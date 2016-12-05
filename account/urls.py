from django.conf.urls import url
from account.views import *

urlpatterns = [
    #Login-Logout Functionality
    # url(r'^login', Login, name='login'),
    # url(r'^logout', Logout, name='logout'),
    url(r'^test', Test, name="test"),
    url(r'^change-password', ChangePassword, name="change_password"),
    url(r'^check-password-ajax', CheckPasswordAjax, name="check_password"),
    url(r'^check-user-email-ajax', CheckUserEmailAjax, name="check_user_email_ajax"),
    ]
