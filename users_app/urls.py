from django.urls import path

from .views import ProfileAPIView, ActivateUser

urlpatterns = [
    path('profile/', ProfileAPIView.as_view()),
    path('auth/users/activate/<uid>/<token>/', ActivateUser.as_view())
]