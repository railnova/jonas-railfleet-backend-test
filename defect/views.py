from rest_framework import viewsets
from defect.models import Defect
from defect.serializers import DefectSerializer
# Create your views here.


class DefectViewSet(viewsets.ModelViewSet):
    queryset = Defect.objects.all()
    serializer_class = DefectSerializer
