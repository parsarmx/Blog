from django.urls import path

from .views import MainAPIView, AddPostAPIView, ViewPostAPIView

urlpatterns = [
    path('', MainAPIView.as_view()),
    path('create/', AddPostAPIView.as_view()),
    path('<str:category>/<int:post_id>/', ViewPostAPIView.as_view())
    ]
