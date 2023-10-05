from django.urls import path
from .views import profile, login_view, register, logout_view

urlpatterns=[
    path("profile/", profile, name="profile"),
    path("login/", login_view, name="login"),
    path("register/", register, name="register"),
    path('logout/', logout_view, name='logout')

]