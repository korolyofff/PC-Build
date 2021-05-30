from django.contrib import admin
from django.urls import path, include
from configurator.views import *


urlpatterns = [
    path('advices', advices_view, name='titles'),
    path('login', login_view, name='login'),
    path('registration', registration_view, name='registration'),
    path('item', item_view, name='item'),
    path('favorits', favorites_view, name='favorites'),
    path('', start_page, name='main')
]
