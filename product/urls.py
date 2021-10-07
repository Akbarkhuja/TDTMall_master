from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView

urlpatterns = [
    path('product/new/', ProductCreateView.as_view(), name='product_new'),
    path('product/<int:pk>/', ProductDetailView.as_view(),
         name='product_detail'),
    path('', ProductListView.as_view(), name='home'),
]