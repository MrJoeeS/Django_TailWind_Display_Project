from django.contrib.auth.models import User, Group
from rest_framework import serializers
from practice_project.models import Usermodel, Datamodel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class Serializationclass(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usermodel
        fields = '__all__'

class DataSerializationclass(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Datamodel
        fields = '__all__'