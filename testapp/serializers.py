from testapp.models import User,Advisor
from rest_framework.serializers import ModelSerializer
class AdvisorSerializer(ModelSerializer):
    class Meta:
        model=Advisor
        fields='__all__'
