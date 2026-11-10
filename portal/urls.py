
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('create/', views.create_item, name='create_item'),

    path('item/<int:id>/', views.item_detail, name='item_detail'),

    path('my-items/', views.my_items, name='my_items'),

    path('edit/<int:id>/', views.edit_item, name='edit_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),

    path('returned/<int:id>/', views.mark_returned, name='mark_returned'),
]
