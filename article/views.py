from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article , ArticleLike,ArticleComment
from .serializers import ArticleSerializer , ArticleLikeSerializer , ArticleCommentSerializer
from rest_framework import status


@api_view(['GET'])
def GetArticle(request , id):

    try:
        article = Article.objects.filter(id = id).first()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)


@api_view(['GET'])
def GetArticles(request):
    try:
        limit = request.GET['limit']
        catagory = request.GET['catagory']
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        articles = Article.objects.filter(catagory=catagory).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if articles.count() >= int(limit):
        articles = articles[0:int(limit)]
    else:
        articles = articles[0:articles.count()]
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def GetArticleComment(request , article_id):
    try:
        articleComment = ArticleComment.objects.filter(article_id = article_id).first()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ArticleCommentSerializer(articleComment)
    return Response(serializer.data)


@api_view(['GET'])
def GetArticleLike(request , article_id):
    try:
        articleLike = ArticleLike.objects.filter(article_id = article_id).all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ArticleLikeSerializer(articleLike , many = True)
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteArticleComment(request , id):
    try:
        articlecomment = ArticleComment.objects.filter(id = id).all()
        articlecomment.delete()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def PostArticleComment(request):
    try:
        serializer = ArticleCommentSerializer(data=request.data )
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(status = status.HTTP_406_NOT_ACCEPTABLE)
    return Response(status=status.HTTP_200_OK)




@api_view(['DELETE'])
def DeleteArticleLike(request , id):
    try:
        articlelikes = ArticleLike.objects.filter(id = id).all()
        articlelikes.delete()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def PostArticleLike(request):
    try:
        serializer = ArticleLikeSerializer(data=request.data )
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(status = status.HTTP_406_NOT_ACCEPTABLE)
    return Response(status=status.HTTP_200_OK)