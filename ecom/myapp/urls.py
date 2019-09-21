from django.urls import path
from . import views

urlpatterns = [
    path('', views.getindex, name='index'),
    path('category/<name>', views.getcategory, name='category'),
    path('product_details/<int:id>', views.Getproduct_details, name='product_details'),
    path('brand/<name>', views.Getbrand, name='brand'),
]
