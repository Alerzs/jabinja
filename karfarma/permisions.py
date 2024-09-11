from rest_framework.permissions import BasePermission
from .models import Karfarma
class IsKarfarma(BasePermission):
    def has_permission(self, request, view):
        try:
            Karfarma.objects.get(user = request.user)
            return True
        except:
            return False