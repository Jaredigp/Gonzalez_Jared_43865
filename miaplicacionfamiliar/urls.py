from django.urls import path, include
from .views import *

urlpatterns = [
    path('',index,name= "inicio"),
    path('ascendencia',ascendencia,name= "ascendencia"),
    path('familia',familia,name="familia"),
    path('ocupacion',ocupacion,name="ocupacion"),
]