from django.urls import path
from.views import Product
urlpatterns = [
    path('All_Product/<int:id>/', Product, name='Product'),
   
]