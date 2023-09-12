from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .serializers import PerevalAddedSerializer, PerevalUpdateSerializer
from .models import PerevalAdded


class SubmitData(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()

    def get_serializer_class(self):
        if self.action == 'update':
            return PerevalUpdateSerializer
        return PerevalAddedSerializer

    def create(self, request, *args, **kwargs):
        serializer = PerevalAddedSerializer(data=request.data)
        instance = self.get_object()
        if serializer.is_valid():
            serializer.save()
            updated_instance = PerevalAdded.objects.get(pk=instance.pk)
            return Response(
                {
                    'state': '1',
                    'message': 'Объект успешно создан',
                    'data': PerevalAddedSerializer(updated_instance).data
                }
            )
        return Response(
            {
                'state': '2',
                'message': 'Не удалось создать объект',
                'data': serializer.errors
            }
        )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PerevalUpdateSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            updated_instance = PerevalAdded.objects.get(pk=instance.pk)
            return Response(
                {
                    'state': '1',
                    'message': 'Изменения успешно применены',
                    'data': PerevalAddedSerializer(updated_instance).data
                }
            )
        return Response(
            {
                'state': '0',
                'message': 'Не удалось применить изменения',
                'errors': serializer.errors
            }
        )
