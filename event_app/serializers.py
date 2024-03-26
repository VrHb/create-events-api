from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework import validators

from .models import Event, Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

    def create(self, validated_data):
        organization = Organization.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            address=validated_data['address'],
            postcode=validated_data['postcode'],
        )
        organization.save()
        return organization

class EventSerializer(serializers.ModelSerializer):
    organizations = OrganizationSerializer(
        read_only=True,
        many=True
    )
    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        event = Event.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            date=validated_data['date']
        # TODO add organizations field from user
        )
        event.save()
        return event
    
