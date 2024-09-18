from django.urls import path
from .views import Login , Register , RequestView , ResumeView , AllOffer, CheckOTP,LoginUser

urlpatterns = [
    path('login/' , LoginUser.as_view()),
    path('checkotp/' , CheckOTP.as_view()),
    path('register/' , Register.as_view()),
    path('job_request/' , RequestView.as_view()),
    path('resume/' , ResumeView.as_view()),
    path('all_offer/' , AllOffer.as_view())
]