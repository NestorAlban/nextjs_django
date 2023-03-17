from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:parent_id>/", views.family, name="index"),
    path("<int:parent_id>/courses", views.courses, name="index"),
    path("<int:parent_id>/enrollements", views.enrollements, name="index"),
    path('parent-views/', ParentViews.as_view()),
    path('courses-views/', CoursesViews.as_view())
]