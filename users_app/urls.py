from django.urls import path

from .views import ProfileAPIView

urlpatterns = [
    path('profile/<str:u_name>/', ProfileAPIView.as_view()),
]