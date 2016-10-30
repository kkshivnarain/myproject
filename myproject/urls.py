"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from mycity.views import OTPView,IWillTrack,CityOverView, CityListView, IssueListView,Index, LoginView, AuthView, UserCreditView, Coordinates

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^accounts/profile/$', Account.as_view()),
#    url(r'^accounts/new/$', NewUser.as_view()),
    url(r'^accounts/otp/$',OTPView.as_view()), #get OTP of existing phone
    url(r'^accounts/otp/(?P<phone>[0-9]+)/$',OTPView.as_view()), #register new phone
    url(r'^accounts/otp/(?P<phone>[0-9]+)/(?P<rcdotp>[0-9]+)?/?$',OTPView.as_view()), #validating otp  
    url(r'^mycity/citylist/$',CityListView.as_view()),
    url(r'^mycity/issuelist/$',IssueListView.as_view()),
    url(r'^mycity/iwilltrack/(?P<phone>[0-9]+)/$',IWillTrack.as_view()),
    url(r'^mycity/overview/(?P<city>[a-z]+)/(?P<category>[a-z]+)/(?P<fdate>[0-9]+)/(?P<tdate>[0-9]+)/$',CityOverView.as_view()),
    url(r'^rest-auth/',include('rest_framework.urls',namespace='rest_framework')),
    url(r'^accounts/auth/$',AuthView.as_view()),
    url(r'^accounts/login/$',LoginView.as_view()),
    url(r'^mycity/score/(?P<phone>[0-9]+)/$',UserCreditView.as_view()),
    url(r'^mycity/coordinates/(?P<city>[a-z]+)/$',Coordinates.as_view()),
	#for webpage
    url(r'^index/$',Index),    
]
