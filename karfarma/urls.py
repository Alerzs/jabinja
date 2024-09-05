from django.urls import path
from .views import *


urlpatterns = [
    path('login/', Login.as_view()),
    path('refresh/', Refresh.as_view()),
    path('myoffer/' , MyOffers.as_view()),
    path('myrequest/' , MyRequests.as_view()),
    path('allkarfarma/' , AllKarfarmas.as_view()),
    path('creatoffer/' , CreateOffer.as_view()),
    path('searchJobOffers/' , SearchJobOffers.as_view()),


]