from django.urls import path
from . import views


urlpatterns = [
    path('newsletter-subscribe/', views.newsletter_signup, name='newsletter-subscribe')
    # path('newsletter-unsubscribe/', views.newsletter_signup, name='newsletter-unsubscribe')
]
