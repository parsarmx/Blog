from django.urls import path

from .views import ProfileAPIView

urlpatterns = [
    path('test/', ProfileAPIView.as_view()),
]