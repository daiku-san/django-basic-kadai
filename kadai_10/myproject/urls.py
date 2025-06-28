from django.contrib import admin
from django.urls import path
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TopView.as_view(), name="top"),
    path('crud/', views.ProductListView.as_view(), name="list"),
    path('crud/new/', views.ProductCreateView.as_view(), name="new"),
    path('crud/edit/<int:pk>/', views.ProductUpdateView.as_view(), name="edit"),
    path('crud/delete/<int:pk>/', views.ProductDeleteView.as_view(), name="delete"),
    path('crud/detail/<int:pk>/', views.ProductDetailView.as_view(), name="detail"),
]