from django.urls import path
from main.views import *


urlpatterns = [ 
    path("" , homepage , name = "home"),
    path("signup" , registerform , name = "register"),
    path("login" , loginform , name = "login"),
    path("logout" , logoutform , name = "logout"),
    path("price" , pricepanel , name = "price"),
    path("ban" , banned , name = "ban"),
    path("news" , newssection , name = "news")
]