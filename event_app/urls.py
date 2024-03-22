from django.urls import path

from .views import EventListView, EventView, CreateOrganizationView, CreateEventView


urlpatterns = [
    path('events/', EventListView.as_view(), name='events'),
    path('organization/', CreateOrganizationView.as_view(), name='create_organization'),
    path('event/', CreateEventView.as_view(), name='create_event'),
    path('event/<int:pk>/', EventView.as_view(), name='event'),
]
