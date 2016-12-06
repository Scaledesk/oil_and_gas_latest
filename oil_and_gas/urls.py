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

    url(r'^login/', Login, name='login'), # Account Views
    url(r'^logout/', Logout, name='logout'), # Account Views

    #Landing page
    url(r'^landing/', Landing, name='landing'),
    url(r'^dashboard/', Dashboard, name='dashboard'),

    #Registration Functionality
    url(r'^create-user-and-claim-company/', CreateUserAndClaimCompany, name="create_user_and_claim_company"),
    url(r'^create-user-and-company/', CreateUserAndCompany, name="create_user_and_company"),
    url(r'^get-company/', GetCompany, name="get_company"),

    #Free
    url(r'^free_field/', FreeField, name="free_field"),

    #Premium
    url(r'^gallery/', Gallery, name="gallery"),
    url(r'^basic_premium_field/', BasicPremiumField, name="basic_premium_field"),
    url(r'^brochure/', Brochure, name="brochure"),

    url(r'^video_link/', VideoLink, name="video_link"),
    url(r'^alliance/', Alliance, "alliance"),
    url(r'^search_alliance/', SearchAlliance, "search_alliance"),


    url(r'^location/', Location, name="location"),
    url(r'^certification/', Certification, name="certification"),
    url(r'^social_link/', SocialLink, name="social_link"),

    #Super PremiumFields
    url(r'^publication/', Publication, name="publication"),
    # url(r'^country', Country),

    #Requirement
    url(r'^post_requirement/', PostRequirement, name="post_requirement"),

    #Search CompanyModel
    url(r'^search_company/', SearchCompany, name="search_company"),
    url(r'^search-company-ajax/', SearchCompanyAjax, name="search_company_ajax"),
    url(r'^check-user-email-ajax/', CheckUserEmailAjax, name="check_user_email_ajax"),
    url(r'^check-company-name-ajax/', CheckCompanyNameAjax, name="check_company_name_ajax"),
    url(r'^check-company-email-ajax/', CheckCompanyEmailAjax, name="check_company_email_ajax"),
    url(r'^test', Test),
    url(r'^test1', Test1),
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static('/libs/', document_root='static/libs/')
# urlpatterns += static('/views/', document_root='static/views/')
urlpatterns += static('/assets/', document_root='static/assets/')
