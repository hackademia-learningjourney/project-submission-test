from django.urls import path
from . import views

urlpatterns = [
    path("",views.projectindex,name="home"),
    path("result/", views.result, name="result"),
   
]
