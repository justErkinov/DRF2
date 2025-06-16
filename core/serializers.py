from rest_framework.serializers import ModelSerializer

from .models import Post,Article

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content']

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'summary', 'content']



# from rest_framework import status

# # 2xx — Muvaffaqiyatli javoblar
# status.HTTP_200_OK              # 200 — So‘rov muvaffaqiyatli bajarildi (GET, PUT, PATCH)
# status.HTTP_201_CREATED         # 201 — Yangi obyekt yaratildi (POST)
# status.HTTP_202_ACCEPTED        # 202 — Qabul qilindi, keyinroq bajariladi
# status.HTTP_204_NO_CONTENT      # 204 — Javob yo‘q, lekin muvaffaqiyatli bajarilgan (DELETE)

# #  4xx — Mijoz (foydalanuvchi) xatolari
# status.HTTP_400_BAD_REQUEST     # 400 — Noto‘g‘ri so‘rov (form xatoliklari)
# status.HTTP_401_UNAUTHORIZED    # 401 — Avtorizatsiya kerak (token yo‘q yoki noto‘g‘ri)
# status.HTTP_403_FORBIDDEN       # 403 — Ruxsat yo‘q (foydalanuvchida huquq yo‘q)
# status.HTTP_404_NOT_FOUND       # 404 — Ma’lumot topilmadi
# status.HTTP_405_METHOD_NOT_ALLOWED # 405 — Bu endpointga bunday metod ruxsat etilmagan

# # 5xx — Server xatolari
# status.HTTP_500_INTERNAL_SERVER_ERROR  # 500 — Serverda ichki xatolik
# status.HTTP_502_BAD_GATEWAY            # 502 — Server noto‘g‘ri javob oldi
# status.HTTP_503_SERVICE_UNAVAILABLE    # 503 — Server vaqtincha ishlamayapti


# return Response({'detail': 'Yaratildi'}, status=status.HTTP_201_CREATED)
# return Response({'error': 'Noto‘g‘ri so‘rov'}, status=status.HTTP_400_BAD_REQUEST)
# return Response({'detail': 'Topilmadi'}, status=status.HTTP_404_NOT_FOUND)
