from rest_framework import renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User, Record
from .serializers import UserSerializer, RecordSerializer, TimelineSerializer


# ModelViewSet provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
class TimelineViewSet(viewsets.ModelViewSet):

    serializer_class = TimelineSerializer
    permission_classes = ()

    @action(methods=['get'], detail=True)
    def aggregate_user_timeline(self, request):
        queryset = Record.objects.filter(user_id = request['user_id']) #all,filter,get,order_by

        return Response(self.get_serializer(queryset))


class RecordViewSet(viewsets.ModelViewSet):

    serializer_class = RecordSerializer
    permission_classes = ()


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    permission_classes = ()

