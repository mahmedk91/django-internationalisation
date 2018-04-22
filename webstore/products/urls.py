from .views import HomeView
from django.urls import path

app_name = 'product'

urlpatterns = [
    path('', view=HomeView.as_view(), name="home"),
]