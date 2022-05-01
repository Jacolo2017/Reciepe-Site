from django.contrib import admin
from meal_plans.models import MealPlan
from meal_plans.views import MealPlan
# Register your models here.


class MealPlanAdmin(admin.ModelAdmin):
    pass


admin.site.register(MealPlan, MealPlanAdmin)

