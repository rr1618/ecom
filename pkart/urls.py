from django.urls import path

from .views import *
app_name = "pkart"
urlpatterns = [
    path('', home, name="home"),
    path('login/', login_request, name="login"),
    path('logout/', logout, name="logout"),
    path('checkout/<int:prod_id>/', checkout, name="checkout")

]
