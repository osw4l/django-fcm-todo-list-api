from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet 
from .serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from apps.app.models import Todo
from rest_framework.decorators import detail_route



class TodoViewSet(ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = Todo.objects.filter(user=self.request.user)
        serializer = TodoSerializer(self.get_queryset(), many=True)
        return Response({
            'todos': serializer.data
        })

    @detail_route(methods=['post'])
    def ready(self, request, pk=None):
        todo = Todo.objects.get(id=pk)
        todo.set_status()
        return Response({
            'ready': True
        })



