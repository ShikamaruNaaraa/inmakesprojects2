from . import views
from django.urls import path

urlpatterns = [

    path('register', views.register, name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    # path('register1',views.register1,name="register1"),
    # path('login1',views.login1,name="login1")
]
