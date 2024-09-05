from django.urls import path
from .views import create_expense, get_expense, delete_expense

urlpatterns = [
    path('expenses/', create_expense, name='create_expense'),
    path('expenses/', get_expense, name='get_expense'),
    path('expenses/<int:id>/', delete_expense, name='delete_expense'),
]
