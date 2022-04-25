from django.urls import path

from tags.views import (
    show_tags,
    TagListView,
    TagDetailView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView
)


urlpatterns = [
    path("", show_tags, name="tags_list"),
    path("", TagListView.as_view(), name="tag_list"),
    path("<int:pk>/", TagDetailView.as_view(), name="tag_detail"),
    path("<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete"),
    path("new/", TagCreateView.as_view(), name="tag_new"),
    path("<int:pk>/edit/", TagUpdateView.as_view(), name="tag_edit"),
]
