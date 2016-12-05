from django.shortcuts import render, render_to_response, HttpResponse, Http404, redirect
# from django.http import HttpResponseRedirect
# from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from pprint import pprint
# from django.utils import simplejson
# import json as simplejson
# from web.utils import CreateCompanyUtil,  CreateUserUtil, CreateCompanyUtil, CreateUserProfileUtil, CreateUserAndCompanyUtil, CreateUserAndClaimCompanyUtil,  CreateUserAndUserProfileUtil# from web.forms import CreateUserForm, CreateCompanyForm, CreateUserAndCompanyForm
# from core.utils import *
# from web.forms import *
from core.models import *


def ContextMaker(request):
    """
    Function to be called to create the context automatically.
    Creates a empty dictionary if no data is found.
    """
    if request.user.is_authenticated():
        u = request.user
        u.up = UserProfile.objects.get(user=u)
        c = CompanyModel.objects.get(owner=u)

        # c.ff = FreeField.objects.get(company=c)
        #
        # c.bpf = BasicPremiumField.object.get(company=c)
        # c.ga = Gallery.objects.filter(company=c) #list
        # c.brochure = Brochure.object.filter(company=c) #list
        # c.vl = VideoLink.objects.filter(company=c) #list
        # c.kc = KeyClient.objects.filter(company=c) #list
        # c.ka = KeyAlliance.objects.filter(company=c) #list
        # c.lo = Location.objects.filter(company=c) #list
        # c.ce = Certification.objects.filter(company=c) #list
        # c.sl = SocialLink.objects.get(company=c)
        #
        # c.pu = Publication.objects.filter(company=c) #list
        # c.re = Requirement.objects.filter(company=c) #list

        context = {'u': u, 'c':c}
    else:
        context={} # empty dictionary in case if user is not authenticated.

    return context
