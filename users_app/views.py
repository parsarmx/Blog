from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


# Create your views here.
class ProfileAPIView(GenericAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, u_name):
        return Response(data={'message': f"Hello {request.user.username}"})
