# pages/urls.py
from django.urls import path

from .views import HomePageView
from .views import AboutPageView
from .views import ContactUsPageView

urlpatterns = [
     path('', HomePageView.as_view(), name='home'),
     path('about/', AboutPageView.as_view(), name='about'),
     path('contactus/', ContactUsPageView.as_view(), name='contactus'),
     ]