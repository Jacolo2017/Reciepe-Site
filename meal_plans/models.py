from django.db import models
from django.conf import settings


USER_MODEL = settings.AUTH_USER_MODEL


class MealPlan(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateField("", auto_now=False)
    owner = models.ForeignKey(
        USER_MODEL,
        related_name="meal_plan",
        on_delete=models.CASCADE,
        null=True
    )
    recipes = models.ManyToManyField("recipes.Recipe",
                                     related_name="mealplan",
                                     )

    def __str__(self):
        return self.name


