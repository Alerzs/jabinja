from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView ,ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Karjoo , Resume ,Request ,User
from .serializer import ResumeSerializer , UserSerializer ,RequestSeializer 
from karfarma.models import Offer
from karfarma.serializer import OfferKarjoo
from .permisions import IsKarjoo
from rest_framework.exceptions import ValidationError , PermissionDenied
from karfarma.views import Login





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
    
    


    
