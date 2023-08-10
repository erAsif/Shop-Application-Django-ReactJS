from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import ProfileSerializer,TimeScheduleSerializer,PerformanceSerializer
from .models import Profile,TimeSchedule,Performance
# authenticate
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ProfileViews(viewsets.ModelViewSet):
    authentication_classes = [ BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # @action(detail=True, methods=['post','get'])
    # def schedule(self,request ):

class ScheduleViews(viewsets.ModelViewSet):
    authentication_classes = [ BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = TimeSchedule.objects.all()
    serializer_class = TimeScheduleSerializer
    http_method_names = ['post','get']

class PerformanceViews(viewsets.ModelViewSet):
    authentication_classes = [ BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    http_method_names = ['post','get']
