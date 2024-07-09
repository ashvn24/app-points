from .views import CustomUserCreate, LoginAPIView
from django.urls.conf import path

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login')
]
