from django.urls import path
# Function views
from pages.views import home, contact, about, login


urlpatterns = [

    # path('', home),
    path('contact/', contact),
    path('about/', about),
    # path('login/', login),
    
    # path('members/', team, name="team"),
    # path('category/<int:cat_id>/member/<int:mem_id>', member, name="member"),

]
