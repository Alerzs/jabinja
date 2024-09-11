from django.urls import path
from .views import Login , Register , RequestView , ResumeView , AllOffer

urlpatterns = [
    path('login/' , Login.as_view()),
    path('register/' , Register.as_view()),
    path('job_request/' , RequestView.as_view()),
    path('resume/' , ResumeView.as_view()),
    path('all_offer/' , AllOffer.as_view())
]