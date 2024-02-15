from . import views
from django.urls import path
from .views import Banner

urlpatterns =[
    path('get/<int:id>' , views.GetBanner),
    path('get/<category>' , views.GetBanners),
]