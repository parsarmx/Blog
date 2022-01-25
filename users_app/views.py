from django.shortcuts import render
import requests

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProfileSerializers
from .models import Profile

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


# Create your views here.
class ProfileAPIView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request):
        try:
            user = Profile.objects.get(username=request.user.username)
            serializers = ProfileSerializers(user)
            return Response(serializers.data)
        except ObjectDoesNotExist:
            return Response(data={"Object Does Not exist": "Line 24 in user_app/views"})


class ActivateUser(APIView):
    def get(self, request, uid, token, format=None):
        payload = {'uid': uid, 'token': token}

        url = "http://localhost:8000/auth/users/activation/"
        response = requests.post(url, data=payload)

        if response.status_code == 204:
            return Response({}, response.status_code)
        else:
            return Response(response.json())
