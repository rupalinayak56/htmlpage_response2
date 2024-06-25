from django.urls import path
from application3.views import *
app_new="anything"
urlpatterns=[
    path('String_3/',String_3,name='String_3'),
    path('Html_3/',Html_3,name="Html_3"),
]