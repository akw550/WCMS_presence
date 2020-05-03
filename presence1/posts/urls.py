from django.urls import path
from posts.views import  new


urlpatterns =[
    # path('index', index ),
    path('new', new)
]