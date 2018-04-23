from .views import HomeView
from django.urls import path
from django.utils.translation import gettext_lazy as _

app_name = 'product'

urlpatterns = [
    path('', view=HomeView.as_view(), name="home"),
    path(_('product.url.products'), view=HomeView.as_view(), name="products"),
]