from . import views
from django.urls import path

urlpatterns = [
    path('get/<int:id>' , views.GetExpert),
    path('tariff/<int:expert_id>' , views.GetTariffs),
    path('collaboration/<int:expert_id>' , views.GetCollaborations),
    path('resume/<int:expert_id>' , views.GetResume),
    path('connecttoexpert/<int:expert_id>' , views.GetConnectToExperts)
]