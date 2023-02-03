from django.urls import path
from .views import BLogListView, BlogDetailView, BlogCreateView, BlogEditView

urlpatterns = [
    path('', BLogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/new/',BlogCreateView.as_view(), name='post_new'),
    path('post/edit/<int:pk>/', BlogEditView.as_view(), name='post_edit'),
]