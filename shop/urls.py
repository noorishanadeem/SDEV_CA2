from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.prod_list, name = 'all_products'),
    path(' <uuid:type_id>/', views.prod_list, name = 'products_by_type'),
    path('<uuid:type_id>/<uuid:product_id>/', views.product_detail, name = 'product_detail'),
]