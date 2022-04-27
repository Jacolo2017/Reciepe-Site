from django.urls import path
from meal_plans.views import (MealPlanCreateView,
                              MealPlanDeleteView,
                              MealPlanDetailView,
                              MealPlanUpdateView,
                              MealPlansListView
                              )


urlpatterns = [
    path("meal_plans", MealPlansListView.as_view(), name="meal_plans_list"),
    path("new/", MealPlanCreateView.as_view(), name="meal_plan_newl"),
    path("<int:pk>/", MealPlanDetailView.as_view(), name="meal_plan_detail"),
    path("<int:pk>/edit", MealPlanUpdateView.as_view(), name="meal_plan_new"),
    path("<int:pk>/delete/",
         MealPlanDeleteView.as_view(),
         name="meal_plan_delete"
         )
]
