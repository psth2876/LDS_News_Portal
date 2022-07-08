from django.urls import path
from .views import index, individual_post

urlpatterns =[
    path('',index,name='index'),
    path('post/<str:slug>/',individual_post,name='individual_post'),
    path('search/',index,name="search_query")
]