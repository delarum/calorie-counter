"""
Forms for the calorie tracker app.

FoodItemForm handles validated user input for adding new food entries.
"""

from django import forms
from .models import FoodItem


class FoodItemForm(forms.ModelForm):
    """
    Form for adding a new food item to today's log.
    Validates that calories are a positive integer and name is non-empty.
    """

    class Meta:
        model = FoodItem
        fields = ['name', 'calories']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g. Chicken breast, 100g',
                'class': 'food-input',
                'autocomplete': 'off',
            }),
            'calories': forms.NumberInput(attrs={
                'placeholder': '250',
                'min': '1',
                'max': '9999',
                'class': 'calorie-input',
            }),
        }
        labels = {
            'name': 'Food Item',
            'calories': 'Calories (kcal)',
        }

    def clean_calories(self):
        """Ensure calorie count is a positive integer."""
        calories = self.cleaned_data.get('calories')
        if calories is not None and calories <= 0:
            raise forms.ValidationError("Calories must be greater than zero.")
        return calories

    def clean_name(self):
        """Strip whitespace and ensure name isn't empty."""
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise forms.ValidationError("Please enter a food name.")
        return name