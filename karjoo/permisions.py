from rest_framework.permissions import BasePermission
from .models import Karjoo

class IsKarjoo(BasePermission):
    def has_permission(self, request, view):
        try:
            Karjoo.objects.get(user = request.user)
            return True
        except:
            return False