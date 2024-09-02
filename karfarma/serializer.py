from rest_framework.serializers import ModelSerializer
from .models import Karfarma , Offer , Request


class KarfarmaSerializer(ModelSerializer):
    class Meta:
        model = Karfarma
        fields = ['name' , 'address' , 'company_description']


class OfferSerializer(ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'
        

class RequestSeializer(ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


