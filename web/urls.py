from django.conf.urls import url
from web.views import *

urlpatterns = [
    #Login-Logout Functionality
    url(r'^login', Login, name='login'),
    url(r'^logout', Logout, name='logout'),

    #Landing page
    url(r'^landing', Landing, name='landing'),
    url(r'^dashboard', Dashboard, name='dashboard'),

    #Registration Functionality
    url(r'^create_user_and_claim_company/', CreateUserAndClaimCompany),
    url(r'^create_user_and_company', CreateUserAndCompany),
    url(r'^get_company/', GetCompany),

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

    url(r'^test', Test),
    ]
