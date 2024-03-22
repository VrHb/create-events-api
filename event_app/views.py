from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .models import Event, Organization
from .serializers import EventSerializer, OrganizationSerializer


class CreateOrganizationView(generics.CreateAPIView):
    queryset = Organization.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = OrganizationSerializer

class CreateEventView(generics.CreateAPIView):
    queryset = Event.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer

class EventPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20

class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'date']
    ordering_fields = ['date',]
    pagination_class = EventPagination

class EventView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer

