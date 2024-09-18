from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView ,ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Karjoo , Resume ,Request ,User
from .serializer import ResumeSerializer , UserSerializer ,RequestSeializer, Otpserializer, OtploginSerializer
from karfarma.models import Offer
from karfarma.serializer import OfferKarjoo
from .permisions import IsKarjoo
from rest_framework.exceptions import ValidationError , PermissionDenied
from karfarma.views import Login
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.views import APIView
import random
from django.core.cache import cache
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken




class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        return Karjoo.objects.create(user = serializer.save())
    

class ResumeView(ListCreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated , IsKarjoo]

    def perform_create(self, serializer):
        my_karjoo = Karjoo.objects.get(user = self.request.user)
        try:
            return serializer.save(karjoo = my_karjoo)
        except:
            raise ValidationError("a resume is already exists")
    
    def get_queryset(self):
        my_karjoo = Karjoo.objects.get(user = self.request.user)
        return Resume.objects.filter(karjoo = my_karjoo)
    

class RequestView(ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSeializer
    permission_classes = [IsAuthenticated , IsKarjoo]

    def perform_create(self, serializer):
        my_karjoo = Karjoo.objects.get(user = self.request.user)
        return serializer.save(karjoo = my_karjoo) 
    
    def get_queryset(self):
        my_karjoo = Karjoo.objects.get(user = self.request.user)
        return Request.objects.filter(karjoo = my_karjoo)
    

class AllOffer(ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferKarjoo
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['date', 'salary']
    search_fields = ['category', 'title']
    filterset_fields = ['category', 'title']
    
class LoginUser(APIView):
    def post(self, request):
        serializer = Otpserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data['phone_number']
        user = User.objects.filter(phone_number=phone_number).first()
        if user:
            otp = random.randint(100000, 999999)
            cache.set(phone_number, otp, timeout=180)
            request.session['phone_number'] = phone_number
            #sms to user
        else:
            return Response({'message': 'Invalid OTP'})


class CheckOTP(APIView):
    def post(self, request):
        serializer = OtploginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = request.session.get('phone_number')
        otp = serializer.validated_data['input_otp']
        cached_otp = cache.get(phone_number)
        if otp == cached_otp:
            cache.delete(phone_number)
            user = User.objects.get(phone_number=phone_number)
            refresh_token = RefreshToken.for_user(user)
            access_token = AccessToken.for_user(user)
            return Response(
                {
                    "refresh_token" : str(refresh_token),
                    "access_token" : str(access_token)
                }
            )        
        else:
            return Response({'message': 'Invalid OTP'})   


    
