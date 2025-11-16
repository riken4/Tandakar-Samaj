from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
        path('', views.home, name='home'), 
        path('about', views.about, name='about'),
        path('team', views.team, name='team'),
        path('team1', views.team1, name='team1'),
        path('shop', views.shop, name='shop'),
        path('product', views.product, name='product'),
        path('event', views.event, name='event'),
]