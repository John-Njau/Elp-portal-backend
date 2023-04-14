from django.contrib import admin

from app.hubs.models import Hub, HubRegister

class HubAdmin(admin.ModelAdmin):
    model = Hub
    list_display = (
        "id",
        "name",
        "description",
        "hub_admin",
    )
    readonly_fields = ("id",)
    list_filter = (
        "name",
    )
    search_fields = (
        "name",
        "description",
    )
    filter_horizontal = ("members",)

class HubRegisterAdmin(admin.ModelAdmin):
    model = HubRegister
    list_display = (
        "id",
        "hub",
        "user",
        "created_at"
    )
    readonly_fields = ("id",)
    list_filter = (
        "hub",
    )
    search_fields = (
        "email",
        "hub",
    )    

admin.site.register(Hub, HubAdmin)
admin.site.register(HubRegister, HubRegisterAdmin)
