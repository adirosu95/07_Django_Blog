from django.urls import path
from . import views


urlpatterns = [
    path(r'newsletter-subscribe/', views.newsletter_signup, name='newsletter-subscribe'),
    path(r'newsletter-unsubscribe/', views.newsletter_unsubscribe, name='newsletter-unsubscribe')
]

