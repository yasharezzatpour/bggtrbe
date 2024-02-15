from . import views
from django.urls import path


urlpatterns = [
    path('get/<int:id>' , views.GetChat),
    path('get/member/<int:id>' , views.GetMember),
    path('get/message/<int:id>' , views.GetMessage),
]