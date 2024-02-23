from . import views
from django.urls import path

urlpatterns = [
    path('get/<int:id>' , views.GetExpert),
    path('tariff/<int:expert_id>' , views.GetTariffs),
    path('collaborationc/<int:expert_id>' , views.GetCollaborationsCount),
    path('resume/<int:expert_id>' , views.GetResume),
    path('connecttoexpert/<int:expert_id>' , views.GetConnectToExperts),
    path('useriexperts' , views.GetUserInterestedExperts),
    path('expertlikec/<int:id>' , views.GetExpertLikesCount)
]