from django.contrib.admin import register, ModelAdmin
from .models import  Offer , Karfarma

@register(Karfarma)
class KarfarmaAdmin(ModelAdmin):
    list_display = [
        'user'
    ]

@register(Offer)
class OfferAdmin(ModelAdmin):
    list_display = [
        'karfarma',
        'date',
        'title',
        'category',
        'description',
        'salary',
        'is_active'
    ]
