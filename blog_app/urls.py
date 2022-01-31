from django.urls import path

from .views import PostAPIView, AddPostAPIView

urlpatterns = [
    path('', PostAPIView.as_view()),
    path('', AddPostAPIView.as_view())
    ]
