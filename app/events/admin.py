from django.contrib import admin

from app.events.models import Event, EventAttendees


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = (
        "id",
        "name",
        "date",
        "time",
        "venue",
        "poster",
        "charges",
        "description",
        "event_creator",
        "event_organizer_name",

    )
    list_filter = (
        "date",
        "event_creator",
        "name",
    )
    search_fields = ("name", "venue", "event_creator")
    ordering = ("-date", "-time")

    readonly_fields = ("id",)
    filter_horizontal = (
        "hubs_invited", "chapters_invited"
    )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related(
            'hubs_invited', 'chapters_invited'
        )

    def event_organizer_name(self, obj):
        if obj.event_organizer == 'hub':
            return obj.event_organizer_object.name
        elif obj.event_organizer == 'chapter':
            return obj.event_organizer_object.name
        elif obj.event_organizer == 'user':
            return obj.event_organizer_object.username
        else:
            return None

    event_organizer_name.admin_order_field = 'event_organizer'
    event_organizer_name.short_description = 'Event Organizer Name'

    # event_organizer_display.short_description = "Event Organizer"


class EventAttendeesAdmin(admin.ModelAdmin):
    model = EventAttendees
    list_display = ("id", "event", "attendee")
    list_filter = ("event", "attendee")
    search_fields = ("event", "attendee")
    ordering = ("event", "attendee")

    readonly_fields = ("id",)

    def get_event(self, obj):
        return obj.event.name

    def get_user(self, obj):
        return obj.user.username

    get_event.short_description = "Event"
    get_user.short_description = "User"


admin.site.register(EventAttendees, EventAttendeesAdmin)

# class TagAdmin(admin.ModelAdmin):
#     model = Tag
#     list_display = ("id", "name")
#     list_filter = ("name",)
#     search_fields = ("name",)
#     ordering = ("name",)

#     readonly_fields = ("id",)

# admin.site.register(Tag, TagAdmin)
