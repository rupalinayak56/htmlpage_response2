from django.urls import path
from application2.views import *
app_new="anthng"
urlpatterns=[
    path('String_2/',String_2,name='String_2'),
    path('Html_2/',Html_2,name="Html_2"),
]