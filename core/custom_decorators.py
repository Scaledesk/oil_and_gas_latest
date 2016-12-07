# from functools import update_wrapper, wraps
# from django.contrib.auth import REDIRECT_FIELD_NAME
# from django.core.urlresolvers import reverse
# from django.http import HttpResponseRedirect
# from django.utils.decorators import available_attrs
# from django.utils.http import urlquote

from django.shortcuts import render, render_to_response, HttpResponse, Http404, redirect
from core.models import *

# def password_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME):
#     """
#     Decorator for views that checks that the user has entered the password,
#     redirecting to the log-in page if necessary.
#     """
#     def _wrapped_view(request, *args, **kwargs):
#         if request.session.get('password_required_auth', False):
#             return view_func(request, *args, **kwargs)
#
#         return HttpResponseRedirect('%s?%s=%s' % (
#             reverse('password_required.views.login'),
#             redirect_field_name,
#             urlquote(request.get_full_path()),
#         ))
#     return wraps(view_func, assigned=available_attrs(view_func))(_wrapped_view)

def premium_required(view_fun):
    """
    Decorator for views that checks if the company is premium, redirecting to the right page if necessary.
    """
    def decorator(request):
        user = request.user
        c = CompanyModel.objects.get(owner=user)
        if c.sub_plan.sub_type=='P' or c.sub_plan.sub_type=='S':
            return view_fun(request)
        else:
            return HttpResponse('premium or super_premium subscription required')
    return decorator

def super_premium_required(view_fun):
    """
    Decorator for views that checks if the company is premium, redirecting to the right page if necessary.
    """
    def decorator(request):
        user = request.user
        c = CompanyModel.objects.get(owner=user)
        if c.sub_plan.sub_type=='S':
            return view_fun(request)
        else:
            return HttpResponse('super premium subscription required')
    return decorator

def requirement_sub_required(view_fun):
    """
    Decorators for the views that check is the company is subscribed to view requirement
    """
    def decorator(request):
        user = request.user
        c = CompnayModel.objects.get(owener=user)
        if c.is_req_sub_acitve:
            return view_fun(request)
        else:
            return HttpResponse('you are not subscribed to view the requirement')
    return decorator
