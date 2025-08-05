from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='products'),
    path("<int:id>/", views.product_detail, name='product_detail'),
    
]