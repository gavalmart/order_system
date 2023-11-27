from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('customers/<str:pk_id>/', views.customers, name='customer'),
    path('products/', views.products, name='product'),
#    path('create_order/', views.createOrder, name='create_order'),
    path('create_order/<str:pk>', views.createOrder, name='create_order'),
    path('update_order/<str:pk>', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>', views.deleteOrder, name='delete_order'),

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    
]