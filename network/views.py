from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .models import NetworkNode
from .serializers import NetworkNodeSerializer, NetworkNodeUpdateSerializer
from .permissions import IsActiveUser, IsAdminUser


class NetworkNodeViewSet(viewsets.ModelViewSet):
    """
    Представления для CRUD операций с NetworkNode.
    """
    queryset = NetworkNode.objects.all()
    permission_classes = [IsActiveUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['contact_info__country']

    def get_serializer_class(self):
        """
        Использует NetworkNodeUpdateSerializer для PUT и PATCH запросов.
        """
        if self.request.method in ['PUT', 'PATCH']:
            return NetworkNodeUpdateSerializer
        return NetworkNodeSerializer

    def get_queryset(self):
        """
        Фильтрует NetworkNode по стране, если передан параметр 'country'.
        """
        queryset = super().get_queryset()
        country = self.request.query_params.get('country', None)
        if country:
            queryset = queryset.filter(contact_info__country=country)
        return queryset

    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def clear_debt(self, request, pk=None):
        """
        Админ-действие для очистки задолженности у выбранного NetworkNode.
        """
        try:
            node = self.get_object()
            node.debt = 0
            node.save()
            return Response({'status': 'Задолженность очищена'})
        except NetworkNode.DoesNotExist:
            return Response({'status': 'Не найдено'}, status=404)

    @action(detail=False, methods=['post'], permission_classes=[IsAdminUser])
    def clear_multiple_debt(self, request):
        """
        Админ-действие для очистки задолженности у нескольких NetworkNode.
        """
        ids = request.data.get('ids', [])
        if not ids:
            return Response(
                {'status': 'Не предоставлены идентификаторы'}, status=400)
        nodes = NetworkNode.objects.filter(id__in=ids)
        if nodes:
            nodes.update(debt=0)
            return Response({'status': 'Задолженности очищены'})
        return Response({'status': 'Звенья не найдены'}, status=404)
