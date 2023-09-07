from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import PerevalAddedSerializer
from .models import PerevalAdded


class SubmitData(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer
