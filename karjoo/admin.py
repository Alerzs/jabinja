from django.contrib.admin import register, ModelAdmin
from .models import Karjoo ,Resume ,Request

@register(Resume)
class ResumeAdmin(ModelAdmin):
    list_display = [
        'gender',
        'address',
        'description',
        'grades',
        'work_filed',
        'work_experience',
    ]



@register(Request)
class RequestAdmin(ModelAdmin):
    list_display = [
        'date',
        'karjoo',
        'offer'
    ]

@register(Karjoo)
class KarjooAdmin(ModelAdmin):
    list_display = [
        'user'
    ]