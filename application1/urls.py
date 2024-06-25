from django.urls import path
from application1.views import *
app_new="nthng"
urlpatterns=[
    path('String_1/',String_1,name='String_1'),
    path('Html_1/',Html_1,name="Html_1"),
]