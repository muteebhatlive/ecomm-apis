# store/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryAPIView.as_view(), name='category-create'),
    path('sub-categories/', SubCategoryAPIView.as_view(), name='subcategory-create'),
    
]
