from django.shortcuts import render
from testapp.models import Candidate,Advisor
from testapp.serializers import AdvisorSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.

class AdvisorCRUDCBV(ModelViewSet):
    queryset=Advisor.objects.all()
    serializer_class=AdvisorSerializer
    authentication_classes=[JSONWebTokenAuthentication,]
    permission_classes=[IsAuthenticated,]
