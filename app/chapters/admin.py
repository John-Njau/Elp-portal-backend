from django.contrib import admin

from app.chapters.models import Chapter, ChapterRegister

class ChapterAdmin(admin.ModelAdmin):
    model = Chapter
    list_display = (
        "name",
        "description",

        "chapter_admin",
        "created_on",
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


class ChapterRegisterAdmin(admin.ModelAdmin):
    model = ChapterRegister
    list_display = (
       
        "id",
        "chapter",
        "user",
        "created_at"
    )
    readonly_fields = ("id",)
    list_filter = (
       
        "chapter",
    )
    search_fields = (
       
        "email",
        "chapter",
    )

admin.site.register(Chapter, ChapterAdmin)
admin.site.register(ChapterRegister, ChapterRegisterAdmin)
