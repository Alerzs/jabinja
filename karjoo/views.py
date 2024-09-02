from rest_framework.generics import ListAPIView, CreateAPIView 
from rest_framework.permissions import IsAuthenticated
from karfarma.models import Request
from karfarma.serializer import RequestSeializer
from . models import Karjoo , Resume
from .serializer import ResumeSerializer , KarjooSerializer



class MyResume(ListAPIView):
    queryset = Karjoo.objects.all()
    serializer_class = KarjooSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Karjoo.objects.filter(user = self.request.user)
    

class NewRequest(CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSeializer
    permission_classes = [IsAuthenticated]


class CreatResume(CreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]
    


