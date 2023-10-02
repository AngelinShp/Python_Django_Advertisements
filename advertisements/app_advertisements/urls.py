from django.urls import path
from .views import index, top_sellers, adv_post

urlpatterns = [
    path('', index, name='main_page'),
    path('top_sellers/', top_sellers, name='top_sellers'),
    path('adv_post/', adv_post, name='adv_post')
]