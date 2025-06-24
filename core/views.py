from django.shortcuts import render

# Create your views here.

from rest_framework import views, viewsets, status
from rest_framework.response import Response

from .serializers import PostSerializer, ArticleSerializer
from .models import Post, Article

#get, post, put, patch, delete



class PostAPIView(views.APIView):
    def get(self, request, pk=None):
        if not pk:
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)
        
        else:
            try:
                post = Post.objects.get(pk=pk)
                serializer = PostSerializer(post)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Post.DoesNotExist:
                return Response({'detail': "Ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)
            
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages)
        

    def put(self, request, pk=None):
        if pk:
            try:
                post = Post.objects.get(pk=pk)
                serializer = PostSerializer(post, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            except Post.DoesNotExist:
                return Response({'detail': "Ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'PUT metodi pk talab qiladi.'})
        
    def patch(self, request, pk=None):
        if pk:
            try:
                post = Post.objects.get(pk=pk)
                serializer = PostSerializer(post, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
            except Post.DoesNotExist:
                return Response({'detail':"Malumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error':'PATCH metodi pk talab qiladi!.'})
        
        
        
    def delete(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk)
            post.delete()
            return Response({'detail': "O'chirildi."})
        except Post.DoesNotExist:
            return Response({'detail': "Ma'lumot topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        
# class ArticleViewSet(viewsets.ViewSet):
#     def list(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
    
#     def retrieve(self, request, pk):
#         article = Article.objects.get(pk=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def create(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.error_messages)

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


    def update(self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
            serializer = ArticleSerializer(article, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Article.DoesNotExist:
            return Response({'detail': "Ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        
    def partial_update(self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
            serializer = ArticleSerializer(article, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Article.DoesNotExist:
            return Response({'detail': "Ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)


    def destroy(self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Article.DoesNotExist:
            return Response({'detail': "Ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)