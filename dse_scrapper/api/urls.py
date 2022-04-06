from django.urls import path

from . import views

urlpatterns = [
    path('share_prices', views.index, name='index'),
    path('top_gainer', views.topGainer, name='top_gainer'),
    path('top_loser', views.topLoser, name='top_loser'),
    path('circuit_breaker/', views.circuitBreaker, name='circuit_breaker'),
]