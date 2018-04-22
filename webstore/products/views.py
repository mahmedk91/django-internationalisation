from django.views.generic import TemplateView
from .models import Product


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        self.extra_context = {'products': products}
        return super().get(request, *args, **kwargs)