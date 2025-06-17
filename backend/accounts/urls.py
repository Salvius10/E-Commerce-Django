from django.urls import path
from .views import RegisterUserView,ProfileUserView,AdminCartView,AdminOrderView,AdminUserView,AdminProductView,AdminUserListView
urlpatterns=[
    path("register/",RegisterUserView.as_view(),name="register"),
    path("profile/", ProfileUserView.as_view(), name="profile"),
    path('admin/user/<int:pk>/', AdminUserView.as_view()),
    path('admin/product/<int:pk>/', AdminProductView.as_view()),
    path('admin/order/<int:pk>/', AdminOrderView.as_view()),
    path('admin/cart/<int:pk>/', AdminCartView.as_view()),
    path('admin/users/', AdminUserListView.as_view()), 



]