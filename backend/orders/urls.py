from django.urls import path
from .views import OrderHistoryView,OrderView,OrderCreateView
urlpatterns=[
    path("view/",OrderView.as_view(),name="order_view"),
    path("history/view/",OrderHistoryView.as_view(),name="order_history"),
    path("create/",OrderCreateView.as_view(),name="order_create"),
]