from . import views
from django.urls import path


urlpatterns = [
    path('userpost/get/<int:id>' , views.GetUserPost ),
    path('userpost/get/' , views.GetUserPosts),
    path('businesspost/get/<int:id>' , views.GetBusinessPost),
    path('businesspost/get/' , views.GetBusinessPosts),
    path('businesspostcomment/get/' , views.GetBusinessPostComments),
    path('businesspostlike/get/' , views.GetBsuinessPostLikes),
]