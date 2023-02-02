from django.urls import path
from .views import BLogListView, BlogDetailView

urlpatterns = [
    path('', BLogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
]