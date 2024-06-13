from django.urls import path
from .views import BlogListAPIView, BlogDetailAPIView, BlogUpdateAPIView, BlogDeleteAPIView, BlogCreateAPIView

urlpatterns = [
    path('list/', BlogListAPIView.as_view(), name='api-list'),
    path('detail/<int:pk>/', BlogDetailAPIView.as_view(), name='api-detail'),
    path('update/<int:pk>/', BlogUpdateAPIView.as_view(), name='api-update'),
    path('delete/<int:pk>/', BlogDeleteAPIView.as_view(), name='api-delete'),
    path('create/', BlogCreateAPIView.as_view(), name='api-create'),
]
