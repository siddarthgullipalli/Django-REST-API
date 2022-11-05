from django.urls import path
from .import views

urlpatterns =[
    path('',views.apioverview , name="api-overview"),
    path('doctors/',views.Doctors , name="doctors"),
    path('doctor/<str:pk>/',views.doctor , name="doctor"),
    path('adddoctor/',views.Adddoctor , name="adddoctor"),
    path('editdoctor/<str:pk>/',views.Editdoctor , name="editdoctor"),
    path('deletedoctor/<str:pk>/',views.deletedoctor , name="deletedoctor"),

]