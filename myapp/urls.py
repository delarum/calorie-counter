"""
URL patterns for the calorie tracker app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:item_id>/', views.delete_food_item, name='delete_food_item'),
    path('reset/', views.reset_log, name='reset_log'),
]