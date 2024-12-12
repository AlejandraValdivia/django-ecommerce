from django.urls import path
from . import views

# app_name = 'store'

urlpatterns = [
    path('', views.store, name='store'),
    # path('category/<slug:slug>', views.category, name='category'),
    # path('product/<slug:slug>', views.product, name='product'),
]