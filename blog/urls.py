from django.urls import path
from .views import BLogListView

urlpatterns = [
    path('', BLogListView.as_view(), name='home'),
]