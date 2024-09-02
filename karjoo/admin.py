from django.contrib.admin import register, ModelAdmin
from .models import Karjoo ,Resume

@register(Karjoo)
class KarjooAdmin(ModelAdmin):
    list_display = [
        'user',
        'resume'
    ]

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



