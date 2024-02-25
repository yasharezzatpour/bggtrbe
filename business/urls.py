from .views import GetBusiness , GetBusinesses
from . import views
from django.urls import path


urlpatterns = [
    path('get/<int:id>' , views.GetBusiness ),
    path('business' , views.GetBusinesses),
    path('capital/get/<int:id>' , views.GetCapital),
    path('income/get/<int:id>' , views.GetIncome),
    path('growth/get/<int:id>' , views.GetGrowth),
    path('staff/get/<int:id>' , views.GetStaff),
    path('comparison/get/<int:id>' ,views.GetComparison),
    path('user/get/<int:owner_id>' , views.GetUserBusiness),
    path('userbusinessinterst/<int:user_id>' , views.GetUserBusinessInterests),
    path('useribusinesses' , views.GetUserInterestedBusinesses),
    path('businesslike/<int:id>' , views.GetBusinessLikes),
    path('businesslike/post/' , views.PostBusinessLike),
    path('businesslike/delete/<int:id>' , views.DeleteBusinessLike),
    path('businesscomment/<int:id>' , views.GetBusinessComments),
    path('businesstag/<int:id>' , views.GetBusinessTags),
    path('businessfollower/<int:id>' , views.GetBusinessFollowers),
    path('businessfollower-delete/<int:id>' , views.DeleteBusienssFollower),
    path('businessfollower-post/' , views.PostBusinessFollower),
    path('businessstaff/<int:id>' , views.GetBusinessStaff),
    path('businesspartnership/<int:id>' , views.GetBusinessPartnerShip),
    path('connecttobusiness/<int:id>' , views.GetConnectToBusiness),
    path('businesscommentlike/<int:id>' , views.GetBusinessCommentLikes),
    path('businesscommentlike-post/' , views.PostBusinessCommentLike),
    path('businesscommentlike-delete/<int:id>' , views.DeleteBusinessCommentLike),
    path('businesscommentdislike/<int:id>' , views.GetBusinessCommentDislikes),
    path('businesscommentdislike-post/' , views.PostBusinessCommentDislike),
    path('businesscommentdislike-delete/<int:id>' , views.DeleteBusinessCommentDislike),
]