from django.urls import path
from .views import Login, Refresh ,MyOffers , MyRequests , AllKarfarmas , CreatOffer


urlpatterns = [
    path('login/', Login.as_view()),
    path('refresh/', Refresh.as_view()),
    path('myoffer/' , MyOffers.as_view()),
    path('myrequest/' , MyRequests.as_view()),
    path('allkarfarma/' , AllKarfarmas.as_view()),
    path('creatoffer/' , CreatOffer.as_view()),
]