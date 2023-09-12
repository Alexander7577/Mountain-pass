from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import PerevalAddedSerializer, PerevalUpdateSerializer
from .models import PerevalAdded


class SubmitData(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()

    def get_serializer_class(self):
        if self.action == 'update':
            return PerevalUpdateSerializer
        return PerevalAddedSerializer
