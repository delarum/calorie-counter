"""
Admin configuration for calorie tracker models.

Registers FoodItem and DailyLog with the Django admin site
for easy data management.
"""

from django.contrib import admin
from .models import DailyLog, FoodItem


class FoodItemInline(admin.TabularInline):
    """Inline editor for food items within a daily log."""
    model = FoodItem
    extra = 0
    readonly_fields = ('added_at',)


@admin.register(DailyLog)
class DailyLogAdmin(admin.ModelAdmin):
    """Admin view for daily logs, with inline food items."""
    list_display = ('date', 'item_count', 'total_calories', 'created_at')
    inlines = [FoodItemInline]


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    """Admin view for individual food items."""
    list_display = ('name', 'calories', 'daily_log', 'added_at')
    list_filter = ('daily_log__date',)
    search_fields = ('name',)