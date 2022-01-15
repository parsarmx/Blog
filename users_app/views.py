from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProfileSerializers
from .models import Profile

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


# Create your views here.
class ProfileAPIView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, u_name):
        user = Profile.objects.get(username=request.user.username)
        serializers = ProfileSerializers(user)
        return Response(serializers.data)
