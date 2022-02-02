from django.urls import path

from .views import MainAPIView, AddPostAPIView

urlpatterns = [
    path('', MainAPIView.as_view()),
    path('', AddPostAPIView.as_view())
    ]
