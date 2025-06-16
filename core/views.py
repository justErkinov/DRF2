from django.shortcuts import render

# Create your views here.

from rest_framework import views, viewsets, status
from rest_framework.response import Response

from .serializers import PostSerializer
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
                serializer = PostSerializer(post, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            except Post.DoesNotExist:
                return Response({'detail': "Ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'PUT metodi pk talab qiladi.'})
        
        
        
    def delete(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk)
            post.delete()
            return Response({'detail': "O'chirildi."})
        except Post.DoesNotExist:
            return Response({'detail': "Ma'lumot topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        
