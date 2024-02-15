from .views import GetArticles , GetArticle
from . import views
from django.urls import path


urlpatterns = [
    path('get/<int:id>' , views.GetArticle ),
    path('article' , views.GetArticles),
    path('articlelike/<int:article_id>' , views.GetArticleLike),
    path('articlecomment/<int:article_id>' , views.ArticleComment),
    path('articlelike-delete/<int:id>' , views.DeleteArticleLike),
    path('articlelike-post/' , views.PostArticleLike),
    path('articlecomment-delete/<int:id>' , views.DeleteArticleComment),
    path('articlecomment-post' , views.PostArticleComment),
]