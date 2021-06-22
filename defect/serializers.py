from django.contrib.auth.models import User
from rest_framework import serializers

from defect.models import Defect


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']


class DefectSerializer(serializers.HyperlinkedModelSerializer):
    # PK because we don't need to return anything sensitive, right?
    # UUID would be nice here
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Defect
        fields = ['comment', 'timestamp', 'user']
