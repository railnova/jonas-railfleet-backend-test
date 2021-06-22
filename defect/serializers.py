from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from defect.models import Defect


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']


class DefectSerializer(serializers.HyperlinkedModelSerializer):
    # PK because we don't need to return anything sensitive, right?
    # UUID would be nice here
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all().order_by('pk'))

    class Meta:
        model = Defect
        fields = ['comment', 'timestamp', 'user']
