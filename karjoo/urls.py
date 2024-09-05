from django.urls import path
from .views import MyResume , NewRequest ,CreatResume, RetriveResume , UpdatemyResume, Myrequest


urlpatterns = [
    path('myresume/', MyResume.as_view()),
    path('newrequest/', NewRequest.as_view()),
    path('creatresume/' , CreatResume.as_view()),
    path('retriveresume/<int:pk>/', RetriveResume.as_view()),
    path('updatemyresume/<int:pk>/', UpdatemyResume.as_view()),
    path('myrequest/' , Myrequest.as_view()),

]