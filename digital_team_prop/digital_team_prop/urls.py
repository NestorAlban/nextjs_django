
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from polls import views

# router_path = routers.DefaultRouter()
# router_path.register()

urlpatterns = [
    path('admin/', admin.site.urls),
    path("polls/", include("polls.urls"))
]
