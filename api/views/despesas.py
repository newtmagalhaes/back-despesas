from rest_framework import viewsets

from ..models import Despesa
from ..serializers import DespesaSerializer


class DespesasView(viewsets.ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
