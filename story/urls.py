from django.urls import path
from . import views

urlpatterns = [
    path ('get/<int:id>' , views.GetStory),
    path('api_key=<api_key>&catagory=<catagory>' , views.PostStory),
    path('storytype' , views.GetStoryTypes),
    path('stories/get/<int:story_type_id>' , views.GetStories),
    path('storylikes/<int:story_id>' , views.GetStoryLikes),
]