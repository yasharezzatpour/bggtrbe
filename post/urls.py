from .views import GetPost
from . import views
from django.urls import path


urlpatterns = [
    path('get/<int:id>' , views.GetPost )
]