from django.urls import path
from . import views

#recipes:recipe
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name = "home"), #Home
    path('<str:category_slug>/', views.category, name = "category"),
    path('recipe/<int:id>/', views.recipe, name = "recipe"),
]
