from rest_framework.generics import ListAPIView, CreateAPIView
from django.http.response import HttpResponse, JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView ,TokenRefreshView
from rest_framework.permissions import IsAuthenticated
from karjoo.models import Request
from karjoo.serializer import RequestSeializer
from .models import  Offer , Karfarma ,User
from .serializer import OfferSerializer , UserSerializer
from rest_framework.generics import ListCreateAPIView
from .permisions import IsKarfarma
import json


class Login(TokenObtainPairView):
    pass

class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        return Karfarma.objects.create(user = serializer.save())

class OfferView(ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated , IsKarfarma]
    ordering_fields = ['price']
    search_fields = ['category']
    filterset_fields = ['category', 'title']

    def get_queryset(self):
        my_karfarma = Karfarma.objects.get(user = self.request.user)
        return Offer.objects.filter(karfarma = my_karfarma)
    
    def perform_create(self, serializer):
        my_karfarma = Karfarma.objects.get(user = self.request.user)
        ser = serializer.save(karfarma = my_karfarma , is_active = True)
        return ser


class MyReq(ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSeializer
    permission_classes = [IsKarfarma , IsAuthenticated]

    def get_queryset(self):
        return Request.objects.filter(offer__karfarma__user = self.request.user)
        
         