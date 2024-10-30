from django.urls import path
from brands.views import BrandListView


urlpatterns = [
    path('brands/list', BrandListView.as_view(), name='brand_list'),
]
