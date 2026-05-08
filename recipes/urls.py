from django.urls import path
from .views import dashboard, manage_recipe, recipe_detail

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('add/', manage_recipe, name='manage_recipe'),
]
