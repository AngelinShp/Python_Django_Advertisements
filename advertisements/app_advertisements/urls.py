from django.urls import path
from .views import index, top_sellers, adv_post, adv_detail

urlpatterns = [
    path('', index, name='main_page'),
    path('top_sellers/', top_sellers, name='top_sellers'),
    path('adv_post/', adv_post, name='adv_post'),
    path('adv/<int:pk>', adv_detail, name='adv_detail')
]