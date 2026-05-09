"""
Views for the calorie tracker app.

Implements full CRUD for food items:
  - index: view today's log and add new items
  - delete_food_item: remove a specific food entry
  - reset_log: clear all entries for today
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import DailyLog, FoodItem
from .forms import FoodItemForm


def index(request):
    """
    Main view: displays today's food items, total calories, and the add form.
    On POST, validates and saves a new food item to today's log.
    """
    # Get or create today's daily log
    today = timezone.localdate()
    daily_log, created = DailyLog.objects.get_or_create(date=today)

    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            food_item = form.save(commit=False)
            food_item.daily_log = daily_log
            food_item.save()
            messages.success(
                request,
                f'"{food_item.name}" ({food_item.calories} kcal) added!'
            )
            return redirect('index')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FoodItemForm()

    food_items = daily_log.food_items.all()
    total_calories = daily_log.total_calories()

    # Daily goal — can be made user-configurable in future iterations
    daily_goal = 2000
    progress_pct = min(int((total_calories / daily_goal) * 100), 100)

    context = {
        'form': form,
        'food_items': food_items,
        'daily_log': daily_log,
        'total_calories': total_calories,
        'daily_goal': daily_goal,
        'progress_pct': progress_pct,
        'today': today,
    }
    return render(request, 'myapp/index.html', context)


@require_POST
def delete_food_item(request, item_id):
    """
    Delete a specific food item from today's log.
    Uses POST (via form) to comply with REST conventions for destructive actions.
    """
    food_item = get_object_or_404(FoodItem, id=item_id)
    name = food_item.name
    food_item.delete()
    messages.success(request, f'"{name}" removed from your log.')
    return redirect('index')


@require_POST
def reset_log(request):
    """
    Reset today's calorie log by deleting all food items for the current day.
    The DailyLog record itself is preserved; only FoodItem entries are removed.
    """
    today = timezone.localdate()
    try:
        daily_log = DailyLog.objects.get(date=today)
        count = daily_log.food_items.count()
        daily_log.food_items.all().delete()
        messages.success(
            request,
            f'Daily log reset. {count} item{"s" if count != 1 else ""} removed.'
        )
    except DailyLog.DoesNotExist:
        messages.info(request, 'Nothing to reset.')

    return redirect('index')