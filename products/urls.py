from . import views
from django.urls import path



urlpatterns=[
    path('',views.index,name="index"),
   path('new',views.indexnew,name="indexnew")
]