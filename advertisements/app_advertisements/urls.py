from django.urls import path
from .views import index, top_sellers

urlpatterns = [
    path('', index, name='main_page'),
    path('top_sellers/', top_sellers, name='top_sellers')
]