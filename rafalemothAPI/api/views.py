from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.serializer import *
from api.models import *

from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

    action_serializers = {
        'retrieve' : RaceDetailsSerializer
    }
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post'])
    def add_data(self, request, pk=None):
        
        #Is the race we're going to use in the queryset (aka exists)
        try:
            q = self.__class__.queryset.get(pk=pk)
        except:
            return Response({'status': 'Invalid race', 'msg': "The race you're trying to add data to does no exist."})

        # The race exists, we can go on
        serializer = DataPointSerializer(data = request.data, many = True)

        if serializer.is_valid():
            for datapoint in serializer.validated_data:
                datapoint.update({"race_id":pk})
            serializer.save()
            return Response({'status': 'Datapoint Valid!', "data": serializer.validated_data})
        else:
            return Response({'status': 'Invalid data', 'error': serializer.errors, 'data':request.data})

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(RaceViewSet, self).get_serializer_class()

class DataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = DataPoint.objects.all()
    serializer_class = DataPointSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
