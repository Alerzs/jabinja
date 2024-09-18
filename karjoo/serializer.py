from rest_framework.serializers import ModelSerializer
from .models import Resume ,Request ,User



class ResumeSerializer(ModelSerializer):
    class Meta:
        model = Resume
        exclude = ["karjoo"]


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

class RequestSeializer(ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

from rest_framework import serializers
class Otpserializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=6)

class OtploginSerializer(serializers.Serializer):
    input_otp = serializers.CharField(max_length=11)