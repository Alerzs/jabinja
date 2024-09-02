from django.contrib.admin import register, ModelAdmin
from .models import Karfarma , Request , Offer


@register(Karfarma)
class KarfarmaAdmin(ModelAdmin):
    list_display = [
        'user',
        'name',
        'address',
        'company_description'
    ]

@register(Request)
class RequestAdmin(ModelAdmin):
    list_display = [
        'date',
        'karjoo',
        'offer'
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
        'status'
    ]
