from rest_framework import serializers
from django.core.files.uploadedfile import InMemoryUploadedFile
from app.events.models import Event, EventAttendees
from app.hubs.models import Hub
from app.chapters.models import Chapter


class EventSerializer(serializers.ModelSerializer):
    event_organizer_name = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            "id",
            "name",
            "date",
            "time",
            "venue",
            "charges",
            "description",
            "poster",
            "event_creator",
            "event_organizer_name",
            "hubs_invited",
            "chapters_invited",

        ]
        read_only_fields = ("id",)

    def get_event_organizer_name(self, obj):
        if obj.event_organizer == "hub":
            return obj.event_organizer_object.name
        elif obj.event_organizer == "chapter":
            return obj.event_organizer_object.name
        elif obj.event_organizer == "user":
            return obj.event_organizer_object.username
        else:
            return None


class EventAdminSerializer(serializers.ModelSerializer):
    """
    Serializes all Event objects
    """

    id = serializers.CharField(read_only=True)
    name = serializers.CharField(required=True)
    event_organizer = serializers.ChoiceField(
        choices=[("hub", "Hub"), ("chapter", "Chapter"), ("user", "User")],
        required=True
    )
    date = serializers.DateField(required=True)
    time = serializers.TimeField(required=True)
    poster = serializers.ImageField(use_url=True)
    venue = serializers.CharField(required=True)
    charges = serializers.FloatField(required=False)
    description = serializers.CharField(required=True)
    hubs_invited = serializers.PrimaryKeyRelatedField(
        queryset=Hub.objects.all(),
        many=True,
        required=False
    )
    chapters_invited = serializers.PrimaryKeyRelatedField(
        queryset=Chapter.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Event
        fields = (
            "id",
            "name",
            "venue",
            "date",
            "time",
            "poster",
            "charges",
            "description",
            "chapters_invited",
            "hubs_invited",
            "event_creator",
            "event_organizer_hub",
            "event_organizer_chapter",
        )
        read_only_fields = ("id",)

    def get_event_organizer_name(self, obj):
        if obj.event_organizer == "hub":
            return obj.event_organizer_object.name
        elif obj.event_organizer == "chapter":
            return obj.event_organizer_object.name
        elif obj.event_organizer == "user":
            return obj.event_organizer_object.username
        else:
            return None

def validate_image(self, image: InMemoryUploadedFile) -> InMemoryUploadedFile:
    if int(image.size) <= 1000000:  # type: ignore[arg-type]
        return image

    raise serializers.ValidationError("Image size must be less than 1MB")


class EventAttendeesSerializer(serializers.ModelSerializer):
    """
    Serializes all EventAttendees objects
    """

    class Meta:
        model = EventAttendees
        fields = (
            "id",
            "event",
            "attendee",
        )
        read_only_fields = ("id",)
