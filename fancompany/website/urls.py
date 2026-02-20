from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('enquiry/<int:product_id>/<str:color>/', views.enquiry, name='enquiry'),
    path('warranty/register/', views.register_warranty, name='register_warranty'),
    path('warranty/status/<str:serial_number>/', views.warranty_status, name='warranty_status'),
    path('warranty/check/', views.check_warranty, name='check_warranty'),

]