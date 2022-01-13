from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class ProfileAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(data={'message': f"Hello {request.user.username}"})
