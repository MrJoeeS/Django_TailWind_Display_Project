import requests
import json

from telnetlib import STATUS
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from practice_project.serializers import UserSerializer, GroupSerializer, Serializationclass, DataSerializationclass
from practice_project.models import Usermodel, Datamodel
from rest_framework.response import Response
from requests.auth import HTTPBasicAuth
import requests
import json


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class UsermodelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users located in the database to be viewed or edited.
    """
    queryset = Usermodel.objects.all()
    serializer_class = Serializationclass
    permission_classes = [permissions.IsAuthenticated]

class DatamodelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows data in the database to be viewed or edited.
    """
    queryset = Datamodel.objects.all()
    serializer_class = DataSerializationclass
    permission_classes = [permissions.IsAuthenticated]

# Create your views here.
def index(request):
    
    """
    Below accesses the API and returns the data in a form that JS can use
    """

    api= 'http://localhost:8000/datamodel/' 

    r = requests.get(api,auth=HTTPBasicAuth('admin','password123'))   # get api response data 
    data = r.json()

    #placeholders
    all_data = []
    label = []
    ad = []

    #This creates the data to use in JS using {{label}} and {{data}}
    for key in range(len(data)-1):
        label.append(key+1)
        all_data.append([data[key+1]['number']])
        ad.append(all_data[key][0])
    return render(request, 'base.html', {'label': json.dumps(label),'data': json.dumps(ad)})

