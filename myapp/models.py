"""
Models for the calorie tracker app.

Defines FoodItem to store daily food entries with calorie counts,
and DailyLog to group entries by date and support reset functionality.
"""

from django.db import models
from django.utils import timezone


class DailyLog(models.Model):
    """
    Represents a single day's calorie tracking session.
    Each log holds multiple food items and can be reset independently.
    """
    date = models.DateField(default=timezone.localdate, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Daily Log — {self.date}"

    def total_calories(self):
        """Calculate the sum of all food item calories for this day."""
        return self.food_items.aggregate(
            total=models.Sum('calories')
        )['total'] or 0

    def item_count(self):
        """Return the number of food items logged today."""
        return self.food_items.count()


class FoodItem(models.Model):
    """
    Represents a single food item entry within a daily log.
    Stores the food name and its calorie value.
    """
    daily_log = models.ForeignKey(
        DailyLog,
        on_delete=models.CASCADE,
        related_name='food_items'
    )
    name = models.CharField(max_length=200)
    calories = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added_at']

    def __str__(self):
        return f"{self.name} ({self.calories} kcal)"