from django.urls import path
from .views import home, order

urlpatterns = [
    path('order', order, name='order'),
    path('', home, name='home'),
]
