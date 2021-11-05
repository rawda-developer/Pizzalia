from django.urls import path
from .views import home, order, edit, pizzas

urlpatterns = [
    path('order', order, name='order'),
    path('pizza/<int:pk>/edit', edit, name='edit'),
    path('pizzas', pizzas, name='pizzas'),
    path('', home, name='home'),
]
