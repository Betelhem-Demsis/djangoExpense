from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('incomes/', include('budgets.urls')),
    path('expenses/', include('expenses.urls')),
    path('admin/', admin.site.urls),
]
