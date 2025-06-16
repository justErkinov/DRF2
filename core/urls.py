from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PostAPIView

# router = DefaultRouter()

# router.register('articles', ArticleViewSet, basename='articles')


urlpatterns = [
    path('posts/', PostAPIView.as_view()),
    path('posts/<int:pk>/', PostAPIView.as_view())
    # path('', include(router.urls))
]