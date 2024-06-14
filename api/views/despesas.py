from rest_framework import pagination, viewsets, response

from ..models import Despesa
from ..serializers import DespesaSerializer


class DespesasView(viewsets.GenericViewSet):
    queryset = Despesa.objects.all().order_by('value')
    pagination_class = pagination.PageNumberPagination
    # serializer_class = DespesaSerializer

    def list(self, request):
        paginate = self.pagination_class()
        result = paginate.paginate_queryset(self.queryset, request=request)
        return response.Response(result)
