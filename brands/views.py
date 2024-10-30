from django.views.generic import ListView
from . import models


class BrandListView(ListView):
    model = models.Brand
    template_name = 'brands_list.html'
    context_object_name = 'brands'