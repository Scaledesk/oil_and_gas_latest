"""test_sub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView
from account.views import *
from web.views import *


urlpatterns = [
    url(r'^account/', include('account.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^web/', include('web.urls')),

    url(r'^login', Login, name='login'), # Account Views
    url(r'^logout', Logout, name='logout'), # Account Views

    #Landing page
    url(r'^landing', Landing, name='landing'),
    url(r'^dashboard', Dashboard, name='dashboard'),

    #Registration Functionality
    url(r'^create-user-and-claim-company/', CreateUserAndClaimCompany),
    url(r'^create-user-and-company', CreateUserAndCompany),
    url(r'^get-company/', GetCompany),

    #Free
    url(r'^free_field', FreeField),

    #Premium
    url(r'^gallery', Gallery),
    url(r'^basic_premium_field', BasicPremiumField),
    url(r'^brochure', Brochure),

    url(r'^video_link', VideoLink),
    url(r'^alliance', Alliance),
    url(r'^search_alliance', SearchAlliance),


    url(r'^location', Location),
    url(r'^certification', Certification),
    url(r'^social_link', SocialLink),

    #Super PremiumFields
    url(r'^publication', Publication),
    # url(r'^country', Country),

    #Requirement
    url(r'^post_requirement', PostRequirement),

    #Search CompanyModel
    url(r'^search_company', SearchCompany),
    url(r'^search-company-ajax', SearchCompanyAjax),
    #
    # url(r'^test', Test),

]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
