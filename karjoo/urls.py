from django.urls import path
from .views import MyResume , NewRequest ,CreatResume


urlpatterns = [
    path('myresume/', MyResume.as_view()),
    path('newrequest/', NewRequest.as_view()),
    path('creatresume/' , CreatResume.as_view()),
]