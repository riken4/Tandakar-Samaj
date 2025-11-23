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
        path('services', views.services, name='services'),
        path('blog', views.blog, name='blog'),
        path('faq', views.faq, name='faq'),
        path('term_of_services', views.term_of_services, name='term_of_services'),
        path('privacy_policy', views.privacy_policy, name='privacy_policy'),
        path('all_product', views.all_product, name='all_product'),


]