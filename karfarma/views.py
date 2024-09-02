from rest_framework.generics import ListAPIView, CreateAPIView
from django.http.response import HttpResponse, JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView ,TokenRefreshView
from rest_framework.permissions import IsAuthenticated
from .models import  Offer , Karfarma , Request
from .serializer import OfferSerializer , KarfarmaSerializer , RequestSeializer
import json


class Login(TokenObtainPairView):
    pass

class Refresh(TokenRefreshView):
    pass


class MyOffers(ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        my_karfarma = Karfarma.objects.get(user = self.request.user)
        return Offer.objects.filter(karfarma = my_karfarma)
    

class MyRequests(ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSeializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        my_karfarma = Karfarma.objects.get(user = self.request.user)
        my_offers = Offer.objects.filter(karfarma = my_karfarma)
        
        return Request.objects.filter(offer = my_offers[0])
        
        
    

class AllKarfarmas(ListAPIView):
    queryset = Karfarma.objects.all()
    serializer_class = KarfarmaSerializer


class CreatOffer(CreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]

    


