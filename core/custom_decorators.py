
# from functools import wraps
#
# from django.conf import settings
# from django.contrib.auth import REDIRECT_FIELD_NAME
# from django.core.exceptions import PermissionDenied
# from django.shortcuts import resolve_url
# from django.utils import six
# from django.utils.decorators import available_attrs
# from django.utils.six.moves.urllib.parse import urlparse
from django.shortcuts import render, render_to_response, HttpResponse, Http404, redirect
from core.models import *

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
