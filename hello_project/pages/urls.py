from django.urls import path

from .views import home_page, menu_page


urlpatterns = [
    path('', home_page, name='home'),
    path('menu/', menu_page, name='menu'),
]
