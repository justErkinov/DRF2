from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Viewlarni import qilamiz
from .views import PostAPIView, ArticleViewSet

# DRF routerni yaratamiz
# Bu avtomatik ravishda /articles/ va /articles/<pk>/ endpointlarni hosil qiladi
router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')

# URL patterns ro‘yxati
urlpatterns = [
    # posts/ — barcha postlar ro‘yxatini olish yoki yangi post yaratish uchun
    path('posts/', PostAPIView.as_view(), name='post-list'),  # GET, POST

    # posts/<int:pk>/ — ma'lum postni ko‘rish, yangilash yoki o‘chirish uchun
    path('posts/<int:pk>/', PostAPIView.as_view(), name='post-detail'),  # GET, PUT, PATCH, DELETE

    # router orqali avtomatik yaratilgan route'larni ulaymiz
    # Bu orqali /articles/ va /articles/<pk>/ endpointlar ishlaydi
    path('', include(router.urls)),
]
