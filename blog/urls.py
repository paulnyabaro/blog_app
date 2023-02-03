from django.urls import path
from .views import BLogListView, BlogDetailView, BlogCreateView, BlogEditView,DeleteView

urlpatterns = [
    path('', BLogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/new/',BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', BlogEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogEditView.as_view(), name='post_delete'),
]