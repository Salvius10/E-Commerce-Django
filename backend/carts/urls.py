from django.urls import path
from .views import CartView,CartItemAddView,CartItemUpdateDeleteView
urlpatterns=[
    path("view/",CartView.as_view(),name="cartview"),
    path("item/view/",CartItemAddView.as_view(),name="itemview"),
    path("item/view/<int:pk>/",CartItemUpdateDeleteView.as_view(),name="cartupdatedelete"),
]