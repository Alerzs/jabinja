from rest_framework.serializers import ModelSerializer
from .models import Resume ,Karjoo



class ResumeSerializer(ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'


class KarjooSerializer(ModelSerializer):
    class Meta:
        model = Karjoo
        fields = '__all__'
