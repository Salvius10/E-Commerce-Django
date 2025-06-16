from django.urls import path
from .views import RegisterUserView,ProfileUserView
urlpatterns=[
    path("register/",RegisterUserView.as_view(),name="register"),
    path("profile/", ProfileUserView.as_view(), name="profile"),

]