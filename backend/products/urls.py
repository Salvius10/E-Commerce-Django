from django.urls import path
from .views import ProductAdminCreate,ProductAdminView,ProductUserView,ProductUserDetailView
urlpatterns=[
    path("view/",ProductUserView.as_view(),name="user_view"),
    path("view/<int:pk>/",ProductUserDetailView.as_view(),name="detail_view"),
    path("admin/view/<int:pk>",ProductAdminView.as_view(),name="admin_edit"),
    path("admin/view/",ProductAdminCreate.as_view(),name="admin_create"),
]