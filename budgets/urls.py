from django.urls import path
from .views import create_income, get_incomes, delete_income

urlpatterns = [
    path('incomes/', create_income, name='create_income'),
    path('incomes/', get_incomes, name='get_incomes'),
    path('incomes/<int:id>/', delete_income, name='delete_income'),
]
