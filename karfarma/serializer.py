from rest_framework.serializers import ModelSerializer
from .models import Karfarma , Offer ,User



class OfferSerializer(ModelSerializer):
    class Meta:
        model = Offer
        exclude = ["karfarma" ]
        

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password"]


class OfferKarjoo(ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'
        